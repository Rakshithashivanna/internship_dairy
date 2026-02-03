class Instagram:
    def __init__(self,title, description,creator_name, location):  
        self.title = title
        self.description = description
        self.likes = 0
        self.comment=[]
        self.creator_name=creator_name
        self.location=location
    def display_title(self):
        print("The title of the reel is ",self.title)
    def display_description(self):
        print("The description of the reel is ",self.description)
    def display_likes(self):
        print("The likes of the reel is ",self.likes)
    def display_creator_name(self):
        print("The creator name of the reel is ",self.creator_name)
    def display_location(self):
        print("The location of the reel is ",self.location)
    def liked(self):
        self.likes += 1
    def disliked(self):
        if self.likes > 0:
            self.likes-=1
    def add_comments(self,commient):
        self.comment.append(commient)
    def display_comment(self):
        comment_count=len(self.comment)
        print("\nThe number of comments is "+ str(comment_count) )
        if comment_count>0:
            for i in range(comment_count):
                print(i,self.comment[i])
        else:
            print("no comment yet")
    def delete_comment(self):
        if len(self.comment)>0:
            deleted_content=self.comment.pop()
            print("The last comment is deleted is",deleted_content)
        else:
            print("NO comment is there")
    


reel1=Instagram("dancing","dancing with friends","Rakshitha Shivanna","Mysore")
reel1.disliked() 
reel1.liked() 




reel2=Instagram("finance minister conference","finance minister conference with friends","Rakshitha Shivanna" ,"Banglore")
reel1.liked() 
reel2.liked() 
reel1.disliked() 
reel1.display_likes()
reel2.display_likes()

reel1.add_comments("Perfect coardination between you")
reel1.display_comment()



reel1.display_creator_name()
reel2.display_creator_name()

reel1.display_location()
reel2.display_location()

reel1.add_comments("It was good")
reel1.display_comment()

reel1.delete_comment()
reel1.display_comment()
