import random

NotNames = ["a", "able", "about", "above", "abst", "accordance", "according", "accordingly", "across", "act", "actually", "added", "adj", "affected", "affecting", "affects", "after", "afterwards", "again", "against", "ah", "all", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "apparently", "approximately", "are", "aren", "arent", "arise", "around", "as", "aside", "ask", "asking", "at", "auth", "available", "away", "awfully", "back", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "being", "believe", "below", "beside", "besides", "between", "beyond", "biol", "both", "brief", "briefly", "but", "by", "ca", "came", "can", "cannot", "can't", "cause", "causes", "certain", "certainly", "co", "com", "come", "comes", "contain", "containing", "contains", "could", "couldnt", "date", "did", "didn't", "different", "do", "does", "doesn't", "doing", "done", "don't", "down", "downwards", "due", "during", "each", "ed", "edu", "effect", "eg", "eight", "eighty", "either", "else", "elsewhere", "end", "ending", "enough", "especially", "et", "et-al", "etc", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "except", "far", "few", "ff", "fifth", "first", "five", "fix", "followed", "following", "follows", "for", "former", "formerly", "forth", "found", "four", "from", "further", "furthermore", "gave", "get", "gets", "getting", "give", "given", "gives", "giving", "go", "goes", "gone", "got", "gotten", "had", "happens", "hardly", "has", "hasn't", "have", "haven't", "having", "he", "hed", "hence", "her", "here", "hereafter", "hereby", "herein", "heres", "hereupon", "hers", "herself", "hes", "hi", "hid", "him", "himself", "his", "hither", "home", "how", "howbeit", "however", "hundred", "id", "ie", "if", "i'll", "im", "immediate", "immediately", "importance", "important", "in", "inc", "indeed", "index", "information", "instead", "into", "invention", "inward", "i", "is", "isn't", "it", "itd", "it'll", "its", "itself", "i've", "just", "keep", "keeps", "kept", "kg", "km", "know", "known", "knows", "largely", "last", "lately", "later", "latter", "latterly", "least", "less", "lest", "let", "lets", "like", "liked", "likely", "line", "little", "'ll", "look", "looking", "looks", "ltd", "made", "mainly", "make", "makes", "many", "may", "maybe", "me", "mean", "means", "meantime", "meanwhile", "merely", "mg", "might", "million", "miss", "ml", "more", "moreover", "most", "mostly", "mr", "mrs", "much", "mug", "must", "my", "myself", "na", "name", "namely", "nay", "nd", "near", "nearly", "necessarily", "necessary", "need", "needs", "neither", "never", "nevertheless", "new", "next", "nine", "ninety", "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "nothing", "now", "nowhere", "obtain", "obtained", "obviously", "of", "off", "often", "oh", "ok", "okay", "old", "omitted", "on", "once", "one", "ones", "only", "onto", "or", "ord", "other", "others", "otherwise", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "owing", "own", "page", "pages", "part", "particular", "particularly", "past", "per", "perhaps", "placed", "please", "plus", "poorly", "possible", "possibly", "potentially", "pp", "predominantly", "present", "previously", "primarily", "probably", "promptly", "proud", "provides", "put", "que", "quickly", "quite", "qv", "ran", "rather", "rd", "re", "readily", "really", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research", "respectively", "resulted", "resulting", "results", "right", "run", "said", "same", "saw", "say", "saying", "says", "sec", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sent", "seven", "several", "shall", "she", "shed", "she'll", "shes", "should", "shouldn't", "show", "showed", "shown", "showns", "shows", "significant", "significantly", "similar", "similarly", "since", "six", "slightly", "so", "some", "somebody", "somehow", "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specifically", "specified", "specify", "specifying", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "sure", "take", "taken", "taking", "tell", "tends", "th", "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that've", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "there'll", "thereof", "therere", "theres", "thereto", "thereupon", "there've", "these", "they", "theyd", "they'll", "theyre", "they've", "think", "this", "those", "thou", "though", "thoughh", "thousand", "throug", "through", "throughout", "thru", "thus", "til", "tip", "to", "together", "too", "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "ts", "twice", "two", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "up", "upon", "ups", "us", "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "value", "various", "'ve", "very", "via", "viz", "vol", "vols", "vs", "want", "wants", "was", "wasnt", "way", "we", "wed", "welcome", "we'll", "went", "were", "werent", "we've", "what", "whatever", "what'll", "whats", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever", "whole", "who'll", "whom", "whomever", "whos", "whose", "why", "widely", "willing", "wish", "with", "within", "without", "wont", "words", "world", "would", "wouldnt", "www", "yes", "yet", "you", "youd", "you'll", "your", "youre", "yours", "yourself", "yourselves", "you've", "zero"]

Yes = ["yes", "yea", "ok", "okey-dokey", "by all means", "affirmative", "aye", "aye aye", "roger", "10-4", "uh-huh", "righto", "very well", "yup", "yuppers", "right on", "ja", "surely", "amen", "fo'shizzle", "totally", "sure", "yessir"]

No = ["no", "uh-uh", "nix", "nixie", "nixy", "nixey", "nope", "nay", "nah", "no way", "no way, jose", "no way jose", "negative", "veto", "out of the question", "no siree", "for foul no fair", "not on your life", "no on your nelly", "no on your tintype", "not for all the tea in china", "not in a million years", "under no circumstances", "not likely", "not for joe", "thumbs down", "pigs might fly", "not a cat in hells chance", "not a cat in hell's chance", "fat chance", "ctach me", "no fear", "go fish"]

Positive = ["good", "nice"]

Negative = ["bad", "horrible"]

#COMMAND Codes are 4 characters
Questions = ["How are you today //NAME//? ", "What have you been doing today? ", "//COMMAND//-JOB-What do you do for a living //NAME//? "]

Responses = [[["Good to hear."], ["That's a shame, at least I am having a good day."], ["What has been happening?"]], [["That sounds great."], ["sounds... interesting."], ["How has that been going?"]], [["Sounds fun"], ["What a bore"], ["What does that involve? "]]]

Name = raw_input("Hello, what is your name? ")

def CalculateName(ReceivedName, Attempt):
    testName = ReceivedName.split(" ")
    if(len(testName) == 1):
        print("Hello " + ReceivedName)
    else:
        toDelete = ["Ignore"]
        for i in range(0, len(testName)):
            if(testName[i].lower() in NotNames):
                toDelete.append(testName[i])
        for i in range(1, len(toDelete)):
            del testName[testName.index(toDelete[i])]
        if(len(testName) > 1):
            UserResponse = raw_input("Is this your full name? ")
            if(UserResponse.lower() in Yes):
                Name = " ".join(testName)
                print("Well hello there " + Name)
            else:
                UserResponse = raw_input("So is your name " + testName[0] + "? ")
                if(UserResponse.lower() in Yes):
                    print("Well hello " + testName[0])
                else:
                    if(Attempt == '1'):
                        UserResponse = raw_input("I'm a bit confused, what is your name?")
                        Name = UserResponse
                        CalculateName(UserResponse, '2')
                    elif(Attempt == '2'):
                        UserResponse = raw_input("Still not understanding you, say it again")
                        Name = UserResponse
                        CalculateName(UserResponse, '3')
                    elif(Attempt == '3'):
                        print("I'm just going to call you Anonymous Guy")
                        Name = "Anonymous Guy"
                        print("Hello " + Name)

CalculateName(Name, '1')
             
AskedQuestions = []

Job = "//UNKNOWN//"

def Command(Question, Response, Attempt):
    Question = Question.replace("//COMMAND//", "")
    Response = Response.split(" ")
    toDelete = ["Ignore"]
    for i in range(0, len(Response)):
        if(Response[i].lower() in NotNames):
            toDelete.append(Response[i])
    for i in range(1, len(toDelete)):
        print(toDelete[i])
        del Response[Response.index(toDelete[i])]
    Response = " ".join(Response)
    if(Question[0:5] == "-JOB-"):
        UserResponse = raw_input("So you are a " + Response + "? ")
        if(UserResponse.lower() in Yes):
            Job = Response
        else:
            if(Attempt == '1'):
                UserResponse = raw_input("So what is you're job? ")
                Command("//COMMAND//" + Question, UserResponse, '2')
            elif(Attempt == '2'):
                UserResponse = raw_input("Then what are you? ")
                Command("//COMMAND//" + Question, UserResponse, '3')
            else:
                UserResponse = raw_input("Just write your job down! ")
                Job = UserResponse

def LookSmart(Response):
    print("I am trying to look smart but my brain seems to be broken today.")
    AskQuestions()

def AskQuestions():
    Question = "Nothing"
    QuestionNum = random.randrange(0, len(Questions))
    if(QuestionNum in AskedQuestions or (Job == "//UNKNOWN//" and "//JOB//" in Questions[QuestionNum])):
        AskQuestions()
    else:
        AskedQuestions.append(QuestionNum)
        Question = Questions[QuestionNum]
        if("//NAME//" in Questions[QuestionNum]):
            Question = Question.replace("//NAME//", Name)
        if("//JOB//" in Questions[QuestionNum]):
            Question = Question.replace("//JOB//", Job)
        if("//COMMAND//" in Questions[QuestionNum]):
            Question = Question.replace("//COMMAND//", "")
            Question = Question[5: ]
#COMMAND Codes are 4 characters
        UserResponse = raw_input(Question)
        if("//COMMAND//" in Questions[QuestionNum]):
            Command(Questions[QuestionNum], UserResponse, '1')
        if(random.randrange(1,5) == 1):
            LookSmart(UserResponse)
        else:
            if(any(word in UserResponse.lower() for word in Positive)):
                if(random.randrange(1,2) == 2):
                    print(Responses[QuestionNum][0][random.randrange(0, len(Responses[QuestionNum][0]))])
                else:
                    raw_input(Responses[QuestionNum][2][random.randrange(0, len(Responses[QuestionNum][2]))])
            elif(any(word in UserResponse for word in Negative)):
                if(random.randrange(1,2) == 2):
                    print(Responses[QuestionNum][1][random.randrange(0, len(Responses[QuestionNum][1]))])
                else:
                    raw_input(Responses[QuestionNum][2][random.randrange(0, len(Responses[QuestionNum][2]))])

            else:
                raw_input(Responses[QuestionNum][2][random.randrange(0, len(Responses[QuestionNum][2]))])
        AskQuestions()


AskQuestions()