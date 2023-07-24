from attrs import define

@define
class Comment:
    ctg: str
    msg: str


class CommentsRepository:
    def __init__(self):
        self.comments = [
            Comment(ctg="Negative",msg="I don't like out educational system" )
        ]
    
    def get_all(self):
        return self.comments
    
    def save(self, comment: Comment):
        self.comments.append(comment)
        return comment


