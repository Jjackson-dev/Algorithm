def solution(record):
    #user_dict = {userID, Nickname}
    user_dict = dict()
    command_dict = {
        "Enter" : "님이 들어왔습니다.",
        "Leave" : "님이 나갔습니다."
    }
    orders = []
    answer = []
    
    #Change the Nickname while for loop 
    for lines in record:
        line = lines.split(" ")
        #Append tuple(userID, command) in order list 
        if line[0] != "Change":
            orders.append((line[1], command_dict[line[0]]))
        #Change Nickname
        if line[0] in ("Enter", "Change"):
            user_dict[line[1]] = line[2]
            
    #Append "user_Nickname + command" in answer  
    for user_id, s in orders:
        answer.append(user_dict[user_id]+s)
    
    return answer
