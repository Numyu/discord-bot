class Node:
    def __init__(self, question, keyword):
        self.question = question
        self.keyword = keyword
        self.list_child_node = []
   
    def insert_node(self, Node, question):
            if self.question == question:
                self.list_child_node.append(Node)
            elif len(self.list_child_node) > 0:
                for child_node in self.list_child_node:
                    child_node.insert_node(Node,question)

    def print(self):
        print(self.question)
        print(self.keyword)
        for child in self.list_child_node:
            child.print()
    
    # Parcourir tout l'arbre
    def node_child(current_node, keyword):
        if len(current_node.list_child_node) > 0:
            for Node in current_node.list_child_node:
                if keyword == Node.keyword:
                    current_node = Node
                    return current_node


    # Code qui fonctionne dans le terminal, commenter la fonction juste au-dessus si vous voulez test et décommenter celle-ci
    # def user_response(self):
    #     print(self.question)
    #     user_answer = input()
    #     for child in self.list_child_node:
    #         if user_answer == child.keyword:
    #             child.user_response()

           
