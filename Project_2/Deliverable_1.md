# Hardik Bhatt

 #Question 1 Answer
 @bhatthardik4 ➜ /workspaces/AlgorithmDS (main) $ git clone https://github.com/microsoft/tinytroupe


 @bhatthardik4 ➜ /workspaces/AlgorithmDS (main) $ cd tinytroupe


 @bhatthardik4 ➜ /workspaces/AlgorithmDS/tinytroupe (main) $ pip install .


 @bhatthardik4 ➜ /workspaces/AlgorithmDS/tinytroupe (main) $ export OPENAI_API_KEY="my_api_key_Hardik"


 >>> lisa_ds = create_lisa_the_data_scientist()
>>> lisa_ds.listen_and_act("Tell me about your life.")


USER --> Lisa Carter: [CONVERSATION] 
          > Tell me about your life.
Lisa Carter acts: [THINK] 
                 > I need to share about my life, including my background, education, and current
                 > job. I should also mention my interests and hobbies to give a well-rounded view.
Lisa Carter acts: [TALK] 
                 > Sure! I grew up in Vancouver, Canada, in a tech-savvy family. My parents were
                 > software engineers, which inspired my interest in technology from a young age. I
                 > pursued a Master's in Data Science at the University of Toronto, where I focused
                 > on improving search relevance using context-aware models. Now, I work as a Data
                 > Scientist at Microsoft in the M365 Search team, analyzing user behavior to
                 > enhance search results. In my free time, I enjoy cooking, playing the piano, and
                 > watching movies, especially comedies and thrillers.
Lisa Carter acts: [DONE] 


>>> from tinytroupe.agent import TinyPerson


>>> hardik = TinyPerson("Hardik")
>>> hardik.define("age", 28)
>>> hardik.define("nationality", "Indian")
>>> hardik.define("occupation", "He is a student in a university.")


>>> hardik.listen_and_act("Tell me about yourself.")

USER --> Hardik: [CONVERSATION] 
          > Tell me about yourself.
Hardik acts: [THINK] 
            > I need to introduce myself. I should mention my name, age, nationality, and what I'm
            > currently doing.
Hardik acts: [TALK] 
            > My name is Hardik, I'm 28 years old, and I'm from India. Currently, I'm a student at a
            > university. I'm really passionate about learning new things and exploring different
            > subjects.
Hardik acts: [DONE] 

>>> from tinytroupe.agent import TinyPerson


>>> terry = TinyPerson("Terry")
>>> terry.define("age", 24) 
>>> terry.define("nationality", "American")
>>> terry.define("occupation", "He is a librarian in a university.")


>>> from tinytroupe.environment import TinyWorld


>>> world = TinyWorld("Classroom", [hardik, terry])
>>> world.make_everyone_accessible()


>>> hardik.listen("I want to keep some books for an extended period")


USER --> Hardik: [CONVERSATION] 
          > I want to keep some books for an extended period
TinyPerson(name='Hardik')

>>> world.run(3)


Hardik acts: [THINK] 
            > The person wants to keep some books for a long time. I should ask them why they want
            > to do that and if they need any help with it.
Hardik acts: [TALK] 
            > That's interesting! Why do you want to keep the books for an extended period? Are you
            > planning to read them again or do you have another reason?
Hardik acts: [DONE] 

Hardik --> Terry: [CONVERSATION] 
            > My name is Hardik, I'm 28 years old, and I'm from India. Currently, I'm a student at a
            > university. I'm really passionate about learning new things and exploring different
            > subjects.
Hardik --> Terry: [CONVERSATION] 
            > That's interesting! Why do you want to keep the books for an extended period? Are you
            > planning to read them again or do you have another reason?
Terry acts: [TALK] 
           > I like to keep books for an extended period because I often find myself wanting to
           > revisit them. Sometimes, I discover new insights or perspectives that I missed the
           > first time. Plus, I just enjoy having them around for reference or inspiration.
Terry acts: [DONE] 

Terry --> Hardik: [CONVERSATION] 
           > I like to keep books for an extended period because I often find myself wanting to
           > revisit them. Sometimes, I discover new insights or perspectives that I missed the
           > first time. Plus, I just enjoy having them around for reference or inspiration.
────────────────────────────────────────────────────────── Classroom step 2 of 3 ───────────────────────────────────────────────────────────
Hardik acts: [THINK] 
            > Terry keeps books for revisiting and gaining new insights. That's a thoughtful
            > approach! I should acknowledge their perspective and maybe share my own thoughts on
            > the value of books.
Hardik acts: [TALK] 
            > That's a great reason to keep books! I completely agree that revisiting them can lead
            > to new insights. Do you have any particular books that you find yourself going back to
            > often?
Hardik acts: [DONE] 

Hardik --> Terry: [CONVERSATION] 
            > That's a great reason to keep books! I completely agree that revisiting them can lead
            > to new insights. Do you have any particular books that you find yourself going back to
            > often?
Terry acts: [TALK] 
           > Yes, I do have a few favorites that I often revisit. One of them is 'To Kill a
           > Mockingbird' by Harper Lee. I find new layers of meaning every time I read it. Another
           > one is '1984' by George Orwell; it always feels relevant no matter the time period.
           > What about you? Do you have any books you go back to?
Terry acts: [DONE] 

Terry --> Hardik: [CONVERSATION] 
           > Yes, I do have a few favorites that I often revisit. One of them is 'To Kill a
           > Mockingbird' by Harper Lee. I find new layers of meaning every time I read it. Another
           > one is '1984' by George Orwell; it always feels relevant no matter the time period.
           > What about you? Do you have any books you go back to?
────────────────────────────────────────────────────────── Classroom step 3 of 3 ───────────────────────────────────────────────────────────
Hardik acts: [THINK] 
            > Terry has some great book choices! 'To Kill a Mockingbird' and '1984' are both
            > classics with deep meanings. I should share my own favorite books and why I like them.
Hardik acts: [TALK] 
            > I really enjoy 'The Alchemist' by Paulo Coelho. It's a beautiful story about following
            > your dreams and finding your personal legend. I also love 'Pride and Prejudice' by
            > Jane Austen; the characters and social commentary are just so engaging. What do you
            > think about those books?
Hardik acts: [DONE] 

Hardik --> Terry: [CONVERSATION] 
            > I really enjoy 'The Alchemist' by Paulo Coelho. It's a beautiful story about following
            > your dreams and finding your personal legend. I also love 'Pride and Prejudice' by
            > Jane Austen; the characters and social commentary are just so engaging. What do you
            > think about those books?
Terry acts: [TALK] 
           > 'The Alchemist' is such an inspiring read! I love how it emphasizes the importance of
           > pursuing one's dreams. As for 'Pride and Prejudice', I appreciate the wit and social
           > commentary as well. Austen's characters are so well-developed and relatable. It's
           > interesting how both books explore personal journeys in different ways. Do you have a
           > favorite character from either of those books?
Terry acts: [DONE] 

Terry --> Hardik: [CONVERSATION] 
           > 'The Alchemist' is such an inspiring read! I love how it emphasizes the importance of
           > pursuing one's dreams. As for 'Pride and Prejudice', I appreciate the wit and social
           > commentary as well. Austen's characters are so well-developed and relatable. It's
           > interesting how both books explore personal journeys in different ways. Do you have a
           > favorite character from either of those books?




Comments: According to me, I approve it as the conversation feels like 2 humans are talking about extending the period of keeping the books and their conversation gets more interesting with the topic and content of the book and it characters.