# mini project
from abc import ABC,abstractmethod


class Tool(ABC):
    def __init__(self,name,description) -> None:
        self.name = name
        self.description = description


    @abstractmethod
    def run(self,*args):
        ...

    
class Calculator(Tool):
    def __init__(self) -> None:
        super().__init__("calculator", "A tool for adding and multiplication")

    def add(self,a , b):
        return a+b

    def multiplication(self,a,b):
        return a*b


    def run(self,*args):
        a , b ,name = args

        if name == "add":
            return self.add(a,b)

        elif name == "mul":
            return self.multiplication(a,b)

        else:
            raise ValueError(f"Invalid operation: {name}")


class GreeterTool(Tool):
    def __init__(self) -> None:
        super().__init__("greeter","A tool for greeting people")
    def run(self,*args):
        name = args[0]

        return f"Hello, {name}"


class Agent:
    def __init__(self,name) -> None:
        self.name = name
        self.tools = []

    def add_tool(self,tool:Tool):
        self.tools.append(tool)


    def list_tool(self):
        for tool in self.tools:
            print(f"{tool.name}, {tool.description}")


        


    def use_tool(self,tool_name:str, *args):
        for tool in self.tools:
            if tool.name == tool_name:
                return tool.run(*args)

        return f"Tool {tool_name} is not found"


agent = Agent("My first agent")
agent.add_tool(Calculator())
agent.add_tool(GreeterTool())
agent.list_tool()

adding = agent.use_tool("calculator",1,3,"mul")

greeting = agent.use_tool("greeter","Amna")

print(adding)
print(greeting)


