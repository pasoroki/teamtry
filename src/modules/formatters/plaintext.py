import json

class Formatter_PlainText:
    '''
    Plain Text
    '''

    def process(self, data: dict) -> dict:
        '''
        Process data
        '''
        print(f"Process Data {data}")
        newdata = json.dumps(data, indent=4)
        # for item in data:
        #     print({item.items()})
        print(f"New data: {newdata}")
        return {"title": "Result", "text": newdata}
