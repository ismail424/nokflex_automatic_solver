from models import Assignment
import requests
import json
import argparse

class Nokflex:
    URL = 'https://nokflex-api.nok.se/api'
    def __init__(self, token: str, assignment_id: id, course_id: int , group_id: int,  debug = False ):        
        self.headers = {
            'Authorization': f'Bearer {token}'
        }
        self.debug = debug        
        self.subpart_id = None
        self.group_id = group_id
        self.course_id = course_id
        self.assignment_id = assignment_id
        
        if debug == False:
            self.data = self.get_data()
        else:
            self.data = self.get_json_file_data()
            
        
    def get_data(self, assignment_id:int = None ):
 
        params = {
            'assignmentId': '',
            'courseId': f'{self.course_id}',
        }
        if assignment_id is not None:
            params['assignmentId'] = assignment_id
        else:
            params['assignmentId'] = self.assignment_id
        

        response = requests.get(f'{self.URL}/v2/assignment/subpart', params=params, headers=self.headers)
        
        if response.status_code == 200:
            response_json = response.json()
            self.subpart_id = response_json['subpart_id']
            return response_json
        
        raise Exception('The request failed with status code ' + str(response.status_code))
    
    def get_json_file_data(self):
        with open('data.json') as f:
            return json.load(f)
        
        
    def get_assignment(self):
        for assignment in self.data['subpart'][0]['assignments']:
            if assignment['assignmentID'] == self.assignment_id:
                return Assignment.from_dict(assignment)
            
        raise Exception('Assignment not found')

    def submit_assignment(self, assignment: Assignment):
        
        params = {
            'courseId': f'{self.course_id}',
        }
        
        json_data = {
            'response': [],
            'slots': [],
            'groupId': f'{self.group_id}',
            'subpartId': f'{self.subpart_id}',
        }

        answer = assignment.content.answer_value
        if len(answer) <= 1:
            json_data['response'] = answer
        else:
            json_data['slots'] = answer
            
        url = f'{self.URL}/v2/assignment/verify/{assignment.assignment_id}'
        
        
        
        response = requests.post(url, params=params, headers=self.headers, json=json_data)
        if response.status_code == 200:
            if response.json()['correct'] == 'true':
                return f'Assignment {assignment.assignment_id} submitted successfully'
            print(json_data)
            return f'Assignment {assignment.assignment_id} submitted but not correct'        
        
        raise Exception('The request failed with status code ' + str(response.status_code))
        


if __name__ == '__main__':
    token = ' token here '
    parser = argparse.ArgumentParser()

    parser._action_groups.pop()
    param = parser.add_argument_group('Arguments:')
    param.add_argument('-a', '--all', help='Submit all assignments')
    param.add_argument('-id','--id', type=int,  help="The assignment id", required=True)
    args = parser.parse_args()
    

    user = Nokflex(token, args.id)
    if args.all is not None:
        for assignment in user.data['subpart'][0]['assignments']:
            print(user.submit_assignment(Assignment.from_dict(assignment)))
    else:
        print("Submit assignment with id: " + str(args.id))
        assignment = user.get_assignment()
        print(user.submit_assignment(assignment))



        
    
    
    


