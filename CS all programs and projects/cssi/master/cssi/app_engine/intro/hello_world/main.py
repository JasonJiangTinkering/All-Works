# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1>Hello, Jason!</h1>')

class AboutPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1>This is the about page</h1>')

class News(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1> This is the news page </h1> ')
        
route = [('/', MainPage), ('/about', AboutPage), ('/news', News)]
app = webapp2.WSGIApplication(route, debug=True)
