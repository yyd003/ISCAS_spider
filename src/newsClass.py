class news:
    def __init__(self):
        self.title = ""
        self.images = ""
        self.content = ""
        self.url = ""
        self.publish_time = ""
        self.author = ""
        self.sources = ""
        self.media_thumb = ""
        self.description = ""

    def __str__(self):
        return "title: " + str(self.title) + " , images: " + str(self.images) + " , content: " + str(self.content) + \
               " , url: " + str(self.url) + " , publish_time: " + str(self.publish_time) + " , author: " + str(self.author) \
               + " , sources: " + str(self.sources)+", media_thumb:"+ str(self.media_thumb)\
               + ", description:" + str(self.description)
