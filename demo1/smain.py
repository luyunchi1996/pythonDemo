class ValProcess:
    def __init__(self,type=str):
        self.type = type
        self.typedict={}
        self.val = ""
        self.typedict[int]={
            "defval":0,
            "nullVal":None
        }
        self.typedict[float] = {
            "defval":0.0,
            "nullVal": None
        }
        self.typedict[str]={
            "defval":"",
            "nullVal":None
        }
        self.typedict[list] = {
            "defval":[],
            "nullVall": None
        }
        self.typedict[tuple]={
            "defval":(),
            "nullVal":None
        }
        self.typedict[set] = {
            "defval": None,
            "nullVal": None
        }
        self.typedict[dict] = {
            "defval": {},
            "nullVal": None
        }
    def setval(self,obj,types=None):
        self.val = obj
        if types != None:
            self.type = types
        types =self.typedict[self.type]
        defVal = types["defval"]
        nullVal = types["nullVal"]

        if obj == nullVal:
            return  defVal
        else:
            codVal = self.setConditionVal()
            if codVal != None:
                return  codVal
            return obj
    def setInt(self,val):
        return self.setval(val,types= int)
    def setFloat(self,val):
        return  self.setval(val,types= float)
    def setStr(self,val):
        return self.setval(val,types= str)
    def setList(self,val):
        return self.setval(val,types= list)
    def setTuple(self,val):
        return  self.setval(val,types= tuple)
    def setSets(self,val):
        return self.setval(val,types= set)
    def setDict(self,val):
        return self.setval(val,types= dict)
    def setConditionVal(self):
        if "condition" not in self.typedict[self.type]:
            return None
        dicts =self.typedict[self.type]["condition"]
        condition = dicts["condition"]
        val = self.val
        if condition == ">":
            if val > dicts["num"]:
               return dicts["val"]
        elif condition == "<":
            if val < dicts["num"]:
                return dicts["val"]
        elif condition == ">=":
            if val >= dicts["num"]:
                return dicts["val"]
        elif condition == "<=":
            if val <= dicts["num"]:
                return dicts["val"]
        elif condition == "==":
            if val == dicts["num"]:
                return dicts["val"]
        elif condition == "!=":
            if val == dicts["num"]:
                return dicts["val"]
        return None
    def setCondition(self,types,num,condition,val):
        self.type = types
        condition ={
            "num":num,
            "condition":condition,
            "val":val
        }
        self.typedict[self.type]["condition"] = condition
        return self
    def setType(self,types,defval,nullVal=None):
        self.type = types
        self.typedict[self.type] = {
            "defval":defval,
            "nullVal":nullVal
        }
        return self

