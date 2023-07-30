import re
from backend.src.parser_generic import MedicalDocParser


class PatientDetailParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name': self.get_name(),
            'patient_number': self.get_number(),
            'patient_vaccinated': self.get_vaccinated(),
            'patient_problems': self.get_problems()
        }


    def get_name(self):
        pattern = 'Date(.*)(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches)>0:
            return matches[0][0].strip()

    def get_number(self):
        pattern = '(\(\d+\) \d+-\d+) Weight'
        matches = re.findall(pattern, self.text)
        if len(matches)>0:
            return matches[0].strip()

    def get_vaccinated(self):
        pattern = 'vaccination\?.*(Yes|No)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches)>0:
            return matches[0].strip()

    def get_problems(self):
        pattern = 'headaches(\)|\}):(.*)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches)>0:
            return matches[0][1].strip()



if __name__ == '__main__':
    document_text1 = '''
    Patient Medical Record
    Patient Information Birth Date
    Jerry Lucas May 2 1998
    (279) 920-8204 Weight:
    4218 Wheeler Ridge Dr 57
    Buffalo, New York, 14201 Height:
    United States gnt
    170
    In Case of Emergency
    eee
    Joe Lucas . 4218 Wheeler Ridge Dr
    Buffalo, New York, 14201
    Home phone United States
    Work phone
    General Medical History
    Chicken Pox (Varicelia): Measles: ..
    IMMUNE NOT IMMUNE
    Have you had the Hepatitis B vaccination?
    Yes
    | List any Medical Problems (asthma, seizures, headaches):
    N/A
    '''
    document_text2 = '''
17/12/2020

Patient Medical Record

Patient Information Birth Date

Kathy Crawford May 6 1972

(737) 988-0851 Weight’

9264 Ash Dr 95

New York City, 10005 '

United States Height:
190

In Case of Emergency
ee J
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone
Genera! Medical History
nn i
Chicken Pox (Varicella): Measies:
IMMUNE

IMMUNE
Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches}:

Migraine'''
    ppd1 = PatientDetailParser(document_text1)
    print(ppd1.parse())
    ppd2 = PatientDetailParser(document_text2)
    print(ppd2.parse())
