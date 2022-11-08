
class BadRequest(Exception):
    def __init__(self, url, data=None, json=None):
        self.message = f"URL: {url}, DATA: {data}, JSON: {json}"
        super().__init__(self.message)


class NotAllArguments(Exception):
    def __init__(self, company_id):

        self.message = f"WBToken or supplier_id doesn't exists {company_id}"
        super().__init__(self.message)


class TooManyTimeOut(Exception):
    def __init__(self, url):
        self.message = f"Too many timeouts by {url}"
        super().__init__(self.message)


class InvalidWBToken(Exception):
    def __init__(self, wb_token=None, supplier_id=None):
        self.message = f"Invalid wb_token: {wb_token} for supplier_id: {supplier_id}"
        super().__init__(self.message)


class InvalidWildAuthNew(Exception):
    def __init__(self):
        self.message = "Invalid wild_auth_new"
        super().__init__(self.message)


class ProxyError(Exception):
    def __init__(self):
        self.message = f"Proxy Error"
        super().__init__(self.message)


class UnknownError(Exception):
    def __init__(self, resp=None):
        self.message = f""
        if resp:
            try:
                self.message += f"status_code {resp.status_code}"
            except:
                pass
            try:
                self.message += f"content {resp.content}"
            except:
                pass
        super().__init__(self.message)


class NoContent(Exception):
    def __init__(self):
        self.message = f""
        super().__init__(self.message)


class TooManyTime(Exception):
    def __init__(self):
        self.message = f""
        super().__init__(self.message)
