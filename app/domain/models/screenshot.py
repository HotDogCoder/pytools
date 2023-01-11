class Screenshot:

    def __init__(self, url, image_name_prefix, driver):
        self.url = url
        self.image_name_prefix = image_name_prefix
        self.driver = driver
        self.image_list = []

