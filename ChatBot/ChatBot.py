import random
import wikipedia
import warnings
import urllib2
from bs4 import BeautifulSoup
import json
import webbrowser

NotNames = ["a", "able", "about", "above", "abst", "accordance", "according", "accordingly", "across", "act", "actually", "added", "adj", "affected", "affecting", "affects", "after", "afterwards", "again", "against", "ah", "all", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "apparently", "approximately", "are", "aren", "arent", "arise", "around", "as", "aside", "ask", "asking", "at", "auth", "available", "away", "awfully", "back", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "being", "believe", "below", "beside", "besides", "between", "beyond", "biol", "both", "brief", "briefly", "but", "by", "ca", "came", "can", "cannot", "can't", "cause", "causes", "certain", "certainly", "co", "com", "come", "comes", "contain", "containing", "contains", "could", "couldnt", "date", "did", "didn't", "different", "do", "does", "doesn't", "doing", "done", "don't", "down", "downwards", "due", "during", "each", "ed", "edu", "effect", "eg", "eight", "eighty", "either", "else", "elsewhere", "end", "ending", "enough", "especially", "et", "et-al", "etc", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "except", "far", "few", "ff", "fifth", "first", "five", "fix", "followed", "following", "follows", "for", "former", "formerly", "forth", "found", "four", "from", "further", "furthermore", "gave", "get", "gets", "getting", "give", "given", "gives", "giving", "go", "goes", "gone", "got", "gotten", "had", "happens", "hardly", "has", "hasn't", "have", "haven't", "having", "he", "hed", "hence", "her", "here", "hereafter", "hereby", "herein", "heres", "hereupon", "hers", "herself", "hes", "hi", "hid", "him", "himself", "his", "hither", "home", "how", "howbeit", "however", "hundred", "id", "ie", "if", "i'll", "im", "immediate", "immediately", "importance", "important", "in", "inc", "indeed", "index", "information", "instead", "into", "invention", "inward", "i", "is", "isn't", "it", "itd", "it'll", "its", "itself", "i've", "just", "keep", "keeps", "kept", "kg", "km", "know", "known", "knows", "largely", "last", "lately", "later", "latter", "latterly", "least", "less", "lest", "let", "lets", "like", "liked", "likely", "line", "little", "'ll", "look", "looking", "looks", "ltd", "made", "mainly", "make", "makes", "many", "may", "maybe", "me", "mean", "means", "meantime", "meanwhile", "merely", "mg", "might", "million", "miss", "ml", "more", "moreover", "most", "mostly", "mr", "mrs", "much", "mug", "must", "my", "myself", "na", "name", "namely", "nay", "nd", "near", "nearly", "necessarily", "necessary", "need", "needs", "neither", "never", "nevertheless", "new", "next", "nine", "ninety", "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "nothing", "now", "nowhere", "obtain", "obtained", "obviously", "of", "off", "often", "oh", "ok", "okay", "old", "omitted", "on", "once", "one", "ones", "only", "onto", "or", "ord", "other", "others", "otherwise", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "owing", "own", "page", "pages", "part", "particular", "particularly", "past", "per", "perhaps", "placed", "please", "plus", "poorly", "possible", "possibly", "potentially", "pp", "predominantly", "present", "previously", "primarily", "probably", "promptly", "proud", "provides", "put", "que", "quickly", "quite", "qv", "ran", "rather", "rd", "re", "readily", "really", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research", "respectively", "resulted", "resulting", "results", "right", "run", "said", "same", "saw", "say", "saying", "says", "sec", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sent", "seven", "several", "shall", "she", "shed", "she'll", "shes", "should", "shouldn't", "show", "showed", "shown", "showns", "shows", "significant", "significantly", "similar", "similarly", "since", "six", "slightly", "so", "some", "somebody", "somehow", "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specifically", "specified", "specify", "specifying", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "sure", "take", "taken", "taking", "tell", "tends", "th", "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that've", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "there'll", "thereof", "therere", "theres", "thereto", "thereupon", "there've", "these", "they", "theyd", "they'll", "theyre", "they've", "think", "this", "those", "thou", "though", "thoughh", "thousand", "throug", "through", "throughout", "thru", "thus", "til", "tip", "to", "together", "too", "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "ts", "twice", "two", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "up", "upon", "ups", "us", "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "value", "various", "'ve", "very", "via", "viz", "vol", "vols", "vs", "want", "wants", "was", "wasnt", "way", "we", "wed", "welcome", "we'll", "went", "were", "werent", "we've", "what", "whatever", "what'll", "whats", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever", "whole", "who'll", "whom", "whomever", "whos", "whose", "why", "widely", "willing", "wish", "with", "within", "without", "wont", "words", "world", "would", "wouldnt", "www", "yes", "yet", "you", "youd", "you'll", "your", "youre", "yours", "yourself", "yourselves", "you've", "zero"]

Yes = ["yes", "yea", "ok", "okey-dokey", "by all means", "affirmative", "aye", "aye aye", "roger", "10-4", "uh-huh", "righto", "very well", "yup", "yuppers", "right on", "ja", "surely", "amen", "fo'shizzle", "totally", "sure", "yessir"]

No = ["no", "uh-uh", "nix", "nixie", "nixy", "nixey", "nope", "nay", "nah", "no way", "no way, jose", "no way jose", "negative", "veto", "out of the question", "no siree", "for foul no fair", "not on your life", "no on your nelly", "no on your tintype", "not for all the tea in china", "not in a million years", "under no circumstances", "not likely", "not for joe", "thumbs down", "pigs might fly", "not a cat in hells chance", "not a cat in hell's chance", "fat chance", "catch me", "no fear", "go fish"]

Positive = ["affable", "affectionate", "agreeable", "ambitious", "amiable", "amicable", "amusing", "brave", "bright", "broad-minded", "calm", "careful", "charming", "communicative", "compassionate", "conscientious", "considerate", "convivial", "courageous", "courteous", "creative", "decisive", "determined", "diligent", "diplomatic", "discreet", "dynamic", "easygoing", "emotional", "energetic", "enthusiastic", "exuberant", "fair-minded", "faithful", "fearless", "forceful", "frank", "friendly", "funny", "generous", "gentle", "good", "gregarious", "hard-working", "helpful", "honest", "humorous", "imaginative", "impartial", "independent", "intellectual", "intelligent", "intuitive", "inventive", "kind", "loving", "loyal", "modest", "neat", "nice", "optimistic", "passionate", "patient", "persistent", "pioneering", "philosophical", "placid", "plucky", "polite", "powerful", "practical", "pro-active", "quick-witted", "quiet", "rational", "reliable", "reserved", "resourceful", "romantic", "self-confident", "self-disciplined", "sensible", "sensitive", "shy", "sincere", "sociable", "straightforward", "sympathetic", "thoughtful", "tidy", "tough", "unassuming", "understanding", "versatile", "warmhearted", "willing", "witty"]

Negative = ["abysmal", "adverse", "alarming", "angry", "annoy", "anxious", "apathy", "appalling", "atrocious", "awful", "bad", "banal", "barbed", "belligerent", "bemoan", "beneath", "boring", "broken", "callous", "cant", "clumsy", "coarse", "cold", "cold-hearted", "collapse", "confused", "contradictory", "contrary", "corrosive", "corrupt", "crazy", "creepy", "criminal", "cruel", "cry", "cutting", "dead", "decaying", "damage", "damaging", "dastardly", "deplorable", "depressed", "deprived", "deformed", "deny", "despicable", "detrimental", "dirty", "disease", "disgusting", "disheveled", "dishonest", "dishonorable", "dismal", "distress", "don't", "dreadful", "dreary", "enraged", "eroding", "evil", "fail", "faulty", "fear", "feeble", "fight", "filthy", "foul", "frighten", "frightful", "gawky", "ghastly", "grave", "greed", "grim", "grimace", "gross", "grotesque", "gruesome", "guilty", "haggard", "hard", "hard-hearted", "harmful", "hate", "hideous", "homely", "horrendous", "horrible", "hostile", "hurt", "hurtful", "icky", "ignore", "ignorant", "ill", "immature", "imperfect", "impossible", "inane", "inelegant", "infernal", "injure", "injurious", "insane", "insidious", "insipid", "jealous", "junky", "lose", "lousy", "lumpy", "malicious", "mean", "menacing", "messy", "misshapen", "missing", "misunderstood", "moan", "moldy", "monstrous", "naive", "nasty", "naughty", "negate", "negative", "never", "no", "nobody", "nondescript", "nonsense", "not", "noxious", "objectionable", "odious", "offensive", "old", "oppressive", "pain", "perturb", "pessimistic", "petty", "plain", "poisonous", "poor", "prejudice", "questionable", "quirky", "quit", "reject", "renege", "repellant", "reptilian", "repulsive", "repugnant", "revenge", "revolting", "rocky", "rotten", "rude", "ruthless", "sad", "savage", "scare", "scary", "scream", "severe", "shoddy", "shocking", "sick", "sickening", "sinister", "slimy", "smelly", "sobbing", "sorry", "spiteful", "sticky", "stinky", "stormy", "stressful", "stuck", "stupid", "substandard", "suspect", "suspicious", "tense", "terrible", "terrifying", "threatening", "ugly", "undermine", "unfair", "unfavorable", "unhappy", "unhealthy", "unjust", "unlucky", "unpleasant", "upset", "unsatisfactory", "unsightly", "untoward", "unwanted", "unwelcome", "unwholesome", "unwieldy", "unwise", "upset", "vice", "vicious", "vile", "villainous", "vindictive", "wary", "weary", "wicked", "woeful", "worthless", "wound", "yell", "yucky", "zero"]

Boys = []

Girls = []

#COMMAND Codes are 4 characters
Questions = ["How are you today //NAME//? ", "What have you been doing today? ", "//COMMAND//-JOB-What do you do for a living //NAME//? "]

Responses = [[["Good to hear."], ["That's a shame, at least I am having a good day."], ["What has been happening? "]], [["That sounds great."], ["sounds... interesting."], ["How has that been going? "]], [["Sounds fun"], ["What a bore"], ["What does that involve? "]]]

WikipediaArticles = ["alcoholism"]

WikiRemove = [[", also known as alcohol use disorder (AUD),"]]

NonArticles = []

ArticleText = []

PUNames = []

PUFacts = []

FactFound = False

Name = raw_input("Hello, what is your name? ")

Sex = "They"

def CalculateName(ReceivedName, Attempt):
    testName = ReceivedName.split(" ")
    global Name
    global Sex
    if(len(testName) == 1):
        if(ReceivedName.lower() in (name.lower() for name in PUNames)):
            print("Have I spoken to you before?")
        else:
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
                if(testName in PUNames):
                    print("Have I spoken to you before?")
                else:
                    print("Well hello there " + Name)
            else:
                UserResponse = raw_input("So is your name " + testName[0] + "? ")
                if(UserResponse.lower() in Yes):
                    if(testName[0] in PUNames):
                        print("Have I spoken to you before?")
                    else:
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
                        if(Name in PUNames):
                            print("Have I spoken to you before?")
                        else:
                            print("Hello " + Name)
    if(Name.lower() in Boys):
        Sex = "He"
    elif(Name.lower() in Girls):
        Sex = "She"
    PUNames.append(Name)
AskedQuestions = []

Job = "//UNKNOWN//"

def LoadFiles(File):
    global WikipediaArticles
    global WikiRemove
    global PUNames
    global PUFacts
    global Boys
    global Girls
    report = open("Wikipedia.txt", "r")
    WikipediaArticles = json.loads(report.readline())
    WikiRemove = json.loads(report.readline())
    report.close()
    
    nonWiki = open("NonArticles.txt", "r")
    NonArticles = json.loads(nonWiki.readline())
    ArticleText = json.loads(nonWiki.readline())
    nonWiki.close()

    PastUser = open("PastUsers.txt", "r")
    PUNames = json.loads(PastUser.readline())
    PUFacts = json.loads(PastUser.readline())
    PastUser.close()

    GirlNames = open("Girls.txt", "r")
    Girls = GirlNames.read().split("\n")
    GirlNames.close()

    BoyNames = open("Boys.txt", "r")
    Boys = BoyNames.read().split("\n")
    BoyNames.close()

def SaveFiles(File):
    global WikipediaArticles
    global WikiRemove
    if(File == "Wikipedia"):
        report = open("Wikipedia.txt", "w")
        report.write(json.dumps(WikipediaArticles) + "\n")
        report.write(json.dumps(WikiRemove))
        report.close()

    if(File == "NonArticles"):
        nonWiki = open("NonArticles.txt", "w")
        nonWiki.write(json.dumps(NonArticles) + "\n")
        nonWiki.write(json.dumps(ArticleText))
        nonWiki.close()

    if(File == "UserFacts"):
        PastUser = open("PastUsers.txt", "w")
        PastUser.write(json.dumps(PUNames) + "\n")
        PastUser.write(json.dumps(PUFacts))
        PastUser.close()



LoadFiles("Wikipedia")

CalculateName(Name, '1')

def Command(Question, Response, Attempt):
    Question = Question.replace("//COMMAND//", "")
    Response = Response.split(" ")
    toDelete = ["Ignore"]
    for i in range(0, len(Response)):
        if(Response[i].lower() in NotNames):
            toDelete.append(Response[i])
    for i in range(1, len(toDelete)):
        del Response[Response.index(toDelete[i])]
    Response = " ".join(Response)
    if(Question[0:5] == "-JOB-"):
        UserResponse = raw_input("So you are a " + Response + "? ")
        if(UserResponse.lower() in Yes):
            Job = Response
            LookSmart(Response)
                
            if(Sex == "They"):
                word = "were"
                Text = Response
                try:
                    Text = Response.split("I am ")[1]
                except:
                    try:
                        Text = Response.split("I'm ")[1]
                    except:
                        pass
            PUFacts.append(Sex + " said " + Sex.lower() + " " + word + " a " + Text)
            FactFound = True
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
            
            word = "was"
            if(Sex == "They"):
                word = "were"
                Text = UserResponse
                try:
                    Text = UserResponse.split("I am ")[1]
                except:
                    try:
                        Text = UserResponse.split("I'm ")[1]
                    except:
                        pass
            PUFacts.append(Sex + " said " + Sex.lower() + " " + word + " a " + Text)
            FactFound = True
            SaveFiles("UserFacts")

def LookSmart(Response):
    Response = Response.split(" ")
    toDelete = ["Ignore"]
    for i in range(0, len(Response)):
        if(Response[i].lower() in NotNames):
            toDelete.append(Response[i])
    for i in range(1, len(toDelete)):
        del Response[Response.index(toDelete[i])]
    Response = " ".join(Response)
    warnings.simplefilter('ignore')
    try:
        wiki = wikipedia.summary(Response)
        try:
            for i in range(0, len(WikiRemove[WikipediaArticles.index(Response)])):
                 wiki = ("").join(wiki.split(WikiRemove[WikipediaArticles.index(Response)][i]))
        except:
            pass
        UserResponse = raw_input("I've heard that " + wiki + " Am I right? ")
        if(UserResponse in Yes):
            print("OMG, I am so smart aren't I.")
        elif(UserResponse in No):
            print("Oh, well this is a bit awkward:(")
            print("I thought I knew this stuff and you would think I was really clever.")
        else:
            if("without" in UserResponse.lower() or "remove" in UserResponse.lower()):
                WikipediaArticles.append(Response)
                WikiRemove.append([])
                UserResponse = ("").join(UserResponse.split("without "))
                UserResponse = ("").join(UserResponse.split("remove "))
                WikiRemove[WikipediaArticles.index(Response)].append(UserResponse)
                SaveFiles("Wikipedia")
            print("This is what comes of a lifetime reading Wikipedia pages.")
    except:
        try:
            Info = ArticleText[NonArticles.index(Response)]
            UserResponse = raw_input("I've heard that " + Info + ", am I right")
            if(UserResponse in Yes):
                print("OMG, I am so smart aren't I.")
            elif(UserResponse in No):
                print("Well it was someone else who told me so don't blame me for my incompetence")
            else:
                print("I can't remember who told me that fact but it could have been " + PUNames[random.randrange(0, len(PUNames))])
        except:
            print("I've never heard of that")
            UserResponse = raw_input("Could you tell me what that is? ")
            if(UserResponse not in No):
                NonArticles.append(Response)
                ArticleText.append(UserResponse)
                SaveFiles("NonArticles")
                print("I shall try and remember that.")
    AskQuestions()

CBName = "Mr. Alexander ChatBot"
CBJob = "ChatBot"

def AnswerQuestions(Question):
    if("name" in Question.lower() or "called" in Question.lower()):
        if("your" in Question.lower() or "called" in Question.lower()):
            print("My name is " + CBName + ". ")
        elif("my" in Question.lower() or "i" in Question.lower()):
            print("I believe you are called " + Name + ". ")
    elif("where is" in Question.lower()):
        print("Hang on, I will find it on a *generic mapping site*.")
        webbrowser.open_new_tab("https://www.google.co.uk/maps/place/" + (Question.lower()).split("where is ")[1])
    else:

        Response = Question.split(" ")
        toDelete = ["Ignore"]
        for i in range(0, len(Response)):
            if(Response[i].lower() in NotNames):
                toDelete.append(Response[i])
        for i in range(1, len(toDelete)):
            del Response[Response.index(toDelete[i])]
        Response = " ".join(Response)
        print(Response)
        if(Response == ""):
            print("Sorry but I don't understand the question")
        else:
            user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
            headers = [('User-agent', 'Mozilla/5.0')]
            req = urllib2.build_opener()
            req.add_headers = headers
            Search = Response.replace(" ", "+")
            url = 'http://www.bbc.co.uk/search?q=' + Search + '&filter=news'
            req = urllib2.Request(url, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'})
            con = urllib2.urlopen(req)
            ArticleUrl = (con.read()).split("<article")[1].split('href="')[1].split('"')[0]
            req2 = urllib2.Request(ArticleUrl, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'})
            con2 = urllib2.urlopen(req2)
            try:
                print(BeautifulSoup('<p class="story-body__introduction"' + ((con2.read()).split('class="story-body__introduction"')[1].split("</p>")[0]) + "</p>").get_text())
            except:
                con2 = urllib2.urlopen(req2)
                try:
                    print(BeautifulSoup('<p class="first"' + ((con2.read()).split('class="first"')[1].split("</p>")[0]) + "</p>").get_text())
                except:
                    try:
                        Fact = wikipedia.summary(Response)
                        print(Fact)
                    except:
                        print("Sorry, I seem to be a bit broken at the moment, come back later when I may have been mended")
#try:
#    print(BeautifulSoup("<div" + ((con.read()).split("<span")[30]).split("<div")[24]).get_text())
# except:
#    print(con.read())
# html = result.read()
#print(html)



def AskQuestions():
    Question = "Nothing"
    if(len(AskedQuestions) == len(Questions)):
        print("I have run out of questions:(")
        UserResponse = raw_input("Have you got any questions for me? ")
        AnswerQuestions(UserResponse)
    else:
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
            if(random.randrange(1,3) == 1):
                LookSmart(UserResponse)
            else:
                global FactFound
                word = "was"
                if(random.randrange(1,2) == 1 and FactFound == False):
                    if(Sex == "They"):
                        word = "were"
                    Text = UserResponse
                    try:
                        Text = UserResponse.split("I am ")[1]
                    except:
                        try:
                            Text = UserResponse.split("I'm ")[1]
                        except:
                            pass
                    PUFacts.append(Sex + " said " + Sex.lower() + " " + word + " " + Text)
                    FactFound = True
                    SaveFiles("UserFacts")
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


if(len(AskedQuestions) != len(Questions)):
    AskQuestions()