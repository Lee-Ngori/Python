class BrowserHistory:
    def __init__(self):
        self.current_page = 'Home'
        self.back_stack = []
    def visit(self,page):
        self.back_stack.append(self.current_page)
        self.current_page  = page
        print(f'Visit:{page}')
    def back(self):
        if self.back_stack:
            previous_page = self.back_stack.pop()
            self.current_page = previous_page
            print(f'Back to:{previous_page}')
        else:
            print('No more history')
    def show_page(self):
        print(f'Current : {self.current_page}')
def test():
    browser = BrowserHistory()
    browser.show_page()           # Current: Home
    browser.visit("News")            # Visit: News
    browser.visit("Video")           # Visit: Video
    browser.visit("Profile")         # Visit: Profile
    browser.back()                   # Back to: Video
    browser.back()                   # Back to: News
    browser.show_page() 
test()

