from scrapy.http import FormRequest
from scrapy.spiders import Spider

class FormSpider(Spider):
    name = 'horseForm'

    start_url = ['https://treehouse-projects.github.io/horse-land/form.html']

    def parse(self, response):
        formdata = {'firstname':'pau',
                    'lastname':'sim',
                    'jobtitle': 'Engineer'}
        return FormRequest.from_response(response, formnumber=0,
                                         formdata=formdata,
                                         callback=self.after_post)

    def after_post(self, response):
        print('\n\n*****************\nForm Processed')
        print(response)
        print('\n*******end******')
