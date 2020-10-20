class Moesi:   
    def __init__(self):
        pass
    
    def getResultingState(self, state, transaction):
        if(state == "I"):
            if(transaction == "PrWr"):
                return ["M","BusRdX"]
            elif(transaction == "PrRd"):
                return ["S","BusRd"]
            elif(transaction == "PrRd(S)"):
                return ["E","BusRd"]
        elif(state == "S"):
            if(transaction == "PrWr"):
                return ["M", "BusUpgr"]
            elif(transaction == "BusRdX"):
                return ["I","flush"]
            elif(transaction == "BusUpgr"):
                return ["I","None"]
            elif(transaction == "PrRd"):
                return ["S","None"]
            elif(transaction == "BusRd"):
                return ["S", "flush"]                
        elif(state == "E"):
            if(transaction == "PrRd"):
                return ["E","None"]
            elif(transaction == "PrWr"):
                return ["M","None"]
            elif(transaction == "BusRd"):
                return ["S","flush"]
            elif(transaction == "BusRdX"):
                return ["I", "flush"]
        elif(state == "M"):
            if(transaction == "BusRd"):
                return ["O","flush"]
            elif(transaction == "BusRdX"):
                return ["I","flush"]
            elif(transaction == "PrRd" or transaction == "PrWr"):
                return ["M", "None"]
        else:
            if(transaction == "PrWr"):
                return ["M","BusUpgr"]
            elif(transaction == "PrRd"):
                return ["O", "None"]
            elif(transaction == "BusRd"):
                return ["O", "flush"]
            elif(transaction == "BusUpgr"):
                return ["O", "None"]

