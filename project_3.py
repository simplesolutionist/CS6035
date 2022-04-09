import hashlib
import math
import random
import sys
# Do NOT alter the import list!!!!


class Project3:

    def __init__(self):
        pass

    # TODO: OPTIONAL - Add helper methods below
    # BEGIN HELPER METHODS
    #return gcd of a and b with euclid algorithm
    #def gcd(a, b):
    #    while b != 0:
    #        c = a % b
    #        a = b
    #        b = c
    #    return a

    def find_modular_inverse(self, x: int, n: int):
        #binary search algorithm
        #pseudocode the lower bound of the binary search algorithm can be set to 0
        # the upper bound can be set to any value
        # while the lower is less than the upper, let middle be equal to the item in the miiddle hence upper + lower // 2
        # check middle element, and check whether element we're searching for matches it, utilize loops for comparison between lower and upper

        #References https://www.tutorialspoint.com/data_structures_algorithms/binary_search_algorithm.htm
        #https://en.wikipedia.org/wiki/Binary_search_algorithm
        upper = 1
        while upper ** n <= x:
            upper *= 2
        lower = upper // 2 
        while lower < upper:
            middle = (lower + upper) // 2
            if lower < middle and middle ** n < x:
                lower = middle
            elif upper > middle and middle ** n > x:
                upper = middle
            else:
                return middle
        return middle + 1


    def get_modular_inverse(self, e: int, phi: int):
        #euclidean algorithm
        #modular inverse of e % phi
        #References https://www.csee.umbc.edu/~chang/cs203.s09/exteuclid.shtml#:~:text=Here's%20the%20pseudo%2Dcode%20for,%2Ct)%20%3B%20%7D%20Note%20that
        #https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm

        #check if prime
        if math.gcd(e, phi) != 1:
            return None

        # Calculate using the Extended Euclidean Algorithm:
        u1 = 1
        u2 = 0 
        u3 = e
        v1 = 0 
        v2 = 1
        v3 = phi

        #if v3 does not equal zero, u3 = v3 * q, find q, find v1, find v2, find v3, as u1,u2,u3 is equal to v1,v2,v3, retun remainder of u1 and phi
        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        return u1 % phi
    # END HELPER METHODS

    def get_factors(self, n: int):
        # TODO: Implement this method for Task 5, Step 1
        p = 0
        q = 0
        for p in range(2, int(math.sqrt(n))+1):
            if n % p == 0:
                q = n // p
                return p, q

    def get_private_key_from_p_q_e(self, p: int, q: int, e: int):
        # TODO: Implement this method for Task 4, Step 2
        d = 0
        phi = (p-1)*(q-1)
        d = self.get_modular_inverse(e, phi)
        return d

    def task_1(self, n_str: str, d_str: str, c_str: str) -> str:
        # TODO: Implement this method for Task 1
        n = int(n_str, 16)
        d = int(d_str, 16)
        c = int(c_str, 16)

        #pseudocode to decrypt cipher integer c with private key d, the plain integer m is c ^ d mod N
        #m = c ** d % n
        #Reference: https://docs.google.com/document/d/1zFBUaH5n4Rghf3G-wJZtVfXrve7m5xMiDUQa0sd05fQ/edit
        #Reference: https://www.journaldev.com/23002/python-pow
        m = pow(c,d,n)

        return hex(m).rstrip('L')

    def task_2(self, password_hash: str) -> str:
        # TODO: Implement this method for Task 2

        # The password list is prepopulated for your convenience
        common_password_list = ['123456', '12345', '123456789', 'password', 'iloveyou', 'princess', '1234567', 'rockyou', '12345678',
                                'abc123', 'nicole', 'daniel', 'babygirl', 'monkey', 'lovely', 'jessica', '654321', 'michael', 'ashley',
                                'qwerty', '111111', 'iloveu', '0', 'michelle', 'tigger', 'sunshine', 'chocolate', 'password1', 'soccer',
                                'anthony', 'friends', 'butterfly', 'purple', 'angel', 'jordan', 'liverpool', 'justin', 'loveme', '123123',
                                'football', 'secret', 'andrea', 'carlos', 'jennifer', 'joshua', 'bubbles', '1234567890', 'superman',
                                'hannah', 'amanda', 'loveyou', 'pretty', 'basketball', 'andrew', 'angels', 'tweety', 'flower', 'hello',
                                'elizabeth', 'hottie', 'tinkerbell', 'charlie', 'samantha', 'barbie', 'chelsea', 'lovers', 'teamo',
                                'jasmine', 'brandon', '666666', 'shadow', 'melissa', 'eminem', 'matthew', 'robert', 'danielle', 'forever',
                                'family', 'jonathan', '987654321', 'computer', 'whatever', 'dragon', 'vanessa', 'cookie', 'naruto',
                                'summer', 'sweety', 'spongebob', 'joseph', 'junior', 'softball', 'taylor', 'yellow', 'daniela', 'lauren',
                                'mickey', 'princesa', 'alexandra', 'alexis', 'jesus', 'estrella', 'miguel', 'william', 'thomas',
                                'beautiful', 'mylove', 'angela', 'poohbear', 'patrick', 'iloveme', 'sakura', 'adrian', 'alexander',
                                'destiny', 'christian', '121212', 'sayang', 'america', 'dancer', 'monica', 'richard', '112233', 'princess1',
                                '555555', 'diamond', 'carolina', 'steven', 'rangers', 'louise', 'orange', '789456', '999999', 'shorty',
                                '11111', 'nathan', 'snoopy', 'gabriel', 'hunter', 'cherry', 'killer', 'sandra', 'alejandro', 'buster',
                                'george', 'brittany', 'alejandra', 'patricia', 'rachel', 'tequiero', '7777777', 'cheese', '159753',
                                'arsenal', 'dolphin', 'antonio', 'heather', 'david', 'ginger', 'stephanie', 'peanut', 'blink182', 'sweetie',
                                '222222', 'beauty', '987654', 'victoria', 'honey', '0', 'fernando', 'pokemon', 'maggie', 'corazon',
                                'chicken', 'pepper', 'cristina', 'rainbow', 'kisses', 'manuel', 'myspace', 'rebelde', 'angel1', 'ricardo',
                                'babygurl', 'heaven', '55555', 'baseball', 'martin', 'greenday', 'november', 'alyssa', 'madison', 'mother',
                                '123321', '123abc', 'mahalkita', 'batman', 'september', 'december', 'morgan', 'mariposa', 'maria',
                                'gabriela', 'iloveyou2', 'bailey', 'jeremy', 'pamela', 'kimberly', 'gemini', 'shannon', 'pictures',
                                'sophie', 'jessie', 'hellokitty', 'claudia', 'babygirl1', 'angelica', 'austin', 'mahalko', 'victor',
                                'horses', 'tiffany', 'mariana', 'eduardo', 'andres', 'courtney', 'booboo', 'kissme', 'harley', 'ronaldo',
                                'iloveyou1', 'precious', 'october', 'inuyasha', 'peaches', 'veronica', 'chris', '888888', 'adriana',
                                'cutie', 'james', 'banana', 'prince', 'friend', 'jesus1', 'crystal', 'celtic', 'zxcvbnm', 'edward',
                                'oliver', 'diana', 'samsung', 'freedom', 'angelo', 'kenneth', 'master', 'scooby', 'carmen', '456789',
                                'sebastian', 'rebecca', 'jackie', 'spiderman', 'christopher', 'karina', 'johnny', 'hotmail', '123456789',
                                'school', 'barcelona', 'august', 'orlando', 'samuel', 'cameron', 'slipknot', 'cutiepie', 'monkey1',
                                '50cent', 'bonita', 'kevin', 'maganda', 'babyboy', 'casper', 'brenda', 'adidas', 'kitten', 'karen',
                                'mustang', 'isabel', 'natalie', 'cuteako', 'javier', '789456123', '123654', 'sarah', 'bowwow', 'portugal',
                                'laura', '777777', 'marvin', 'denise', 'tigers', 'volleyball', 'jasper', 'rockstar', 'january', 'alicia',
                                'nicholas', 'flowers', 'cristian', 'tintin', 'bianca', 'chrisbrown', 'chester', '101010', 'smokey',
                                'silver', 'internet', 'sweet', 'strawberry', 'garfield', 'dennis', 'panget', 'francis', 'cassie', 'benfica',
                                'love123', 'asdfgh', 'lollipop', 'olivia', 'cancer', 'camila', 'qwertyuiop', 'superstar', 'harrypotter',
                                'charles', 'monique', 'midnight', 'vincent', 'christine', 'apples', 'scorpio', 'jordan23', 'lorena',
                                'andreea', 'mercedes', 'katherine', 'charmed', 'abigail', 'rafael', 'icecream', 'mexico', 'brianna',
                                'nirvana', 'aaliyah', 'pookie', 'johncena', 'lovelove', 'abcdef', 'benjamin', '131313', 'gangsta', 'brooke',
                                '333333', 'hiphop', 'aaaaaa', 'mybaby', 'sergio', 'welcome', 'metallica', 'julian', 'travis', 'myspace1',
                                'babyblue', 'sabrina', 'michael1', 'jeffrey', 'stephen', 'love', 'dakota', 'catherine', 'badboy',
                                'fernanda', 'westlife', 'blondie', 'sasuke', 'smiley', 'jackson', 'simple', 'melanie', 'steaua', 'dolphins',
                                'roberto', 'fluffy', 'teresa', 'piglet', 'ronald', 'slideshow', 'asdfghjkl', 'minnie', 'newyork', 'jason',
                                'raymond', 'santiago', 'jayson', '88888888', '5201314', 'jerome', 'gandako', 'muffin', 'gatita', 'babyko',
                                '246810', 'sweetheart', 'chivas', 'ladybug', 'kitty', 'popcorn', 'alberto', 'valeria', 'cookies', 'leslie',
                                'jenny', 'nicole1', '12345678910', 'leonardo', 'jayjay', 'liliana', 'dexter', '232323', 'amores', 'rockon',
                                'christ', 'babydoll', 'anthony1', 'marcus', 'fatima', 'miamor', 'lover', 'chris1', 'single', 'eeyore',
                                'lalala', '252525', 'scooter', 'natasha', 'skittles', 'brooklyn', 'colombia', '159357', 'teddybear',
                                'winnie', 'happy', 'manutd', '123456a', 'britney', 'katrina', 'christina', 'pasaway', 'cocacola', 'mahal',
                                'grace', 'linda', 'albert', 'tatiana', 'london', 'cantik', '123456', 'lakers', 'marie', 'teiubesc',
                                '147258369', 'charlotte', 'natalia', 'francisco', 'amorcito', 'smile', 'paola', 'angelito', 'manchester',
                                'hahaha', 'elephant', 'mommy1', 'shelby', '147258', 'kelsey', 'genesis', 'amigos', 'snickers', 'xavier',
                                'turtle', 'marlon', 'linkinpark', 'claire', 'stupid', '147852', 'marina', 'garcia', 'diego', 'brandy',
                                'letmein', 'hockey', '444444', 'sharon', 'bonnie', 'spider', 'iverson', 'andrei', 'justine', 'frankie',
                                'pimpin', 'disney', 'rabbit', '54321', 'fashion', 'soccer1', 'red123', 'bestfriend', 'england', 'hermosa',
                                '456123', 'qazwsx', 'bandit', 'danny', 'allison', 'emily', '102030', 'lucky1', 'sporting', 'miranda',
                                'dallas', 'hearts', 'camille', 'wilson', 'potter', 'pumpkin', 'iloveu2', 'number1', 'katie', 'guitar',
                                '212121', 'truelove', 'jayden', 'savannah', 'hottie1', 'phoenix', 'monster', 'player', 'ganda', 'people',
                                'scotland', 'nelson', 'jasmin', 'timothy', 'onelove', 'ilovehim', 'shakira', 'estrellita', 'bubble',
                                'smiles', 'brandon1', 'sparky', 'barney', 'sweets', 'parola', 'evelyn', 'familia', 'love12', 'nikki',
                                'motorola', 'florida', 'omarion', 'monkeys', 'loverboy', 'elijah', 'joanna', 'canada', 'ronnie', 'mamita',
                                'emmanuel', 'thunder', '999999999', 'broken', 'rodrigo', 'maryjane', 'westside', 'california', 'lucky',
                                'mauricio', 'yankees', 'jamaica', 'justin1', 'amigas', 'preciosa', 'shopping', 'flores', 'mariah', 'matrix',
                                'isabella', 'tennis', 'trinity', 'jorge', 'sunflower', 'kathleen', 'bradley', 'cupcake', 'hector',
                                'martinez', 'elaine', 'robbie', 'friendster', 'cheche', 'gracie', 'connor', 'hello1', 'valentina', 'melody',
                                'darling', 'sammy', 'jamie', 'santos', 'abcdefg', 'joanne', 'candy', 'loser', 'dominic', 'pebbles',
                                'sunshine1', 'swimming', 'millie', 'loving', 'gangster', 'blessed', 'compaq', 'taurus', 'gloria', 'tyler',
                                'aaron', 'darkangel', 'kitkat', 'megan', 'dreams', 'sweetpea', 'bettyboop', 'jessica1', 'cynthia',
                                'cheyenne', 'ferrari', 'dustin', 'iubire', 'a123456', 'snowball', 'purple1', 'violet', 'darren', 'starwars',
                                'bestfriends', 'inlove', 'kelly', 'batista', 'karla', 'sophia', 'chacha', 'marian', 'sydney', 'pogiako',
                                'gerald', 'jordan1', '10203', 'daddy1', 'zachary', 'daddysgirl', 'billabong', 'carebear', 'froggy', 'pinky',
                                'erika', 'oscar', 'skater', 'raiders', 'nenita', 'tigger1', 'ashley1', 'charlie1', 'gatito', 'lokita',
                                'maldita', 'buttercup', 'nichole', 'bambam', 'nothing', 'glitter', 'bella', 'amber', 'apple', '123789',
                                'sister', 'zacefron', 'tokiohotel', 'loveya', 'lindsey', 'money', 'lovebug', 'bubblegum', 'marissa',
                                'dreamer', 'darkness', 'cecilia', 'lollypop', 'nicolas', 'google', 'lindsay', 'cooper', 'passion',
                                'kristine', 'green', 'puppies', 'ariana', 'chubby', 'raquel', 'lonely', 'anderson', 'sammie', 'mario',
                                'butter', 'willow', 'roxana', 'mememe', 'caroline', 'susana', 'kristen', 'baller', 'hotstuff', 'carter',
                                'stacey', 'babylove', 'angelina', 'miller', 'scorpion', 'sierra', 'sweet16', '12345', 'rocker', 'bhebhe',
                                'gustavo', 'marcos', 'chance', '123qwe', 'kayla', 'james1', 'football1', 'eagles', 'loveme1', 'milagros',
                                'stella', 'lilmama', 'beyonce', 'lovely1', 'rocky', 'daddy', 'catdog', 'armando', 'margarita', '151515',
                                'loves', 'lolita', '202020', 'gerard', 'undertaker', 'amistad', 'williams', 'qwerty1', 'freddy',
                                'capricorn', 'caitlin', 'bryan', 'delfin', 'dance', 'cheerleader', 'password2', 'PASSWORD', 'martha',
                                'lizzie', 'georgia', 'matthew1', 'enrique', 'zxcvbn', 'badgirl', 'andrew1', '141414', '11111111', 'dancing',
                                'cuteme', 'booger', 'amelia', 'vampire', 'skyline', 'chiquita', 'angeles', 'scoobydoo', 'janine', 'tamara',
                                'carlitos', 'money1', 'sheila', 'justme', 'ireland', 'kittycat', 'hotdog', 'yamaha', 'tristan', 'harvey',
                                'israel', 'legolas', 'michelle1', 'maddie', 'angie', 'cinderella', 'lester', 'ashton', 'tazmania',
                                'remember', 'xxxxxx', 'tekiero', 'thebest', 'princesita', 'lucky7', 'peewee', 'paloma', 'buddy1', 'deedee',
                                'miriam', 'april', 'patches', 'regina', 'janice', 'cowboys', 'myself', 'lipgloss', 'jazmin', 'rosita',
                                'happy1', 'felipe', 'chichi', 'pangit', 'mierda', 'genius', '741852963', 'hernandez', 'awesome', 'walter',
                                'tinker', 'arturo', 'silvia', 'melvin', 'celeste', 'pussycat', 'gorgeous', 'david1', 'molly', 'honeyko',
                                'mylife', 'animal', 'penguin', 'babyboo', 'loveu', 'simpsons', 'lupita', 'boomer', 'panthers', 'hollywood',
                                'alfredo', 'musica', 'johnson', 'hawaii', 'sparkle', 'kristina', 'crazy', 'valerie', 'spencer', 'scarface',
                                'hardcore', '98765', '0', 'winter', 'hailey', 'trixie', 'hayden', 'micheal', 'wesley', '242424',
                                '987654321', 'marisol', 'nikita', 'daisy', 'jeremiah', 'pineapple', 'mhine', 'isaiah', 'christmas', 'cesar',
                                'lolipop', 'butterfly1', 'chloe', 'lawrence', 'xbox360', 'sheena', 'murphy', 'madalina', 'anamaria',
                                'gateway', 'debbie', 'blonde', 'jasmine1', 'please', 'bubbles1', 'jimmy', 'beatriz', 'diamonds', 'whitney',
                                'friendship', 'sweetness', 'pauline', 'desiree', 'trouble', '741852', 'united', 'marley', 'brian',
                                'barbara', 'hannah1', 'bananas', 'julius', 'leanne', 'sandy', 'marie1', 'anita', 'lover1', 'chicago',
                                'twinkle', 'pantera', 'february', 'birthday', 'shadow1', 'qwert', 'bebita', '87654321', 'twilight',
                                'imissyou', 'pollito', 'ashlee', 'tucker', 'cookie1', 'shelly', 'catalina', '147852369', 'beckham',
                                'simone', 'nursing', 'iloveyou!', 'eugene', 'torres', 'damian', '123123123', 'joshua1', 'bobby', 'babyface',
                                'andre', 'donald', 'daniel1', 'panther', 'dinamo', 'mommy', 'juliana', 'cassandra']

        password = common_password_list[0]
        # This is how you get the SHA-256 hash:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        #pseudocode for/while passwords found in the common_password_list provide
        # if the SHA-256 hash of the password is equal to the hash of a randomly selected password from the list
        # return the plaintext password

        #References: https://www.unf.edu/~broggio/cop3530/2220pseu.htm
        #https://www.simplilearn.com/tutorials/cyber-security-tutorial/sha-256-algorithm

        for password in common_password_list:
           if hashlib.sha256(password.encode()).hexdigest() == password_hash:
            return password

    def task_3(self, user_id_1: str, user_id_2: str, amount: int, prev_block_hash: str) -> int:
        # TODO: Implement this method for Task 3

        #pseudocode valid block concatenated(+) with transaction string and hash of previous block
        # nonce + transaction string which is user_id_1 + user_id_2 + amount + prev_block_hash, be aware of str and int
        # nonce needs to be declared to 0
        # utilize a loop (for/while) that calculates a valid block and produces a SHA256 hash of the block
        # if the two integers/digits contained in the hash block are leading zeroos or 00,
        # return the nonce or else increment nonce value

        #References https://en.wikipedia.org/wiki/Cryptographic_nonce
        #https://coincentral.com/what-is-a-nonce-proof-of-work/

        nonce = 0
        while 1:
            valid_block = str(nonce)+user_id_1+':'+user_id_2+':'+str(amount)+prev_block_hash
            hash_block = hashlib.sha256(valid_block.encode()).hexdigest()
            if hash_block[:2] == '00':
                return nonce
            else:
                nonce += 1

    def task_4(self, from_user_id: str, to_user_id: str, amount: int, d: int, e: int, n: int) -> int:
        # TODO: Implement this method for Task 4

        # Build the transaction string
        trans = from_user_id + ':' + to_user_id + ':' + str(amount)
        # Hash the transaction string
        trans_hash = hashlib.sha256(trans.encode('utf-8'))
        # You may find this line helpful for getting the integer value of the transaction hash
        trans_hash_as_int = int.from_bytes(trans_hash.digest(), sys.byteorder)

        # Create the signature (the number 11 is simply a placeholder)

        #pseudocode similar to task 1
        #utilize pow function to sign a transaction
        # trans_hash is the hashed transaction string
        #to decrypt cipher integer c with private key d, the plain integer m is c ^ d mod N
        #signature = integer value of hashed transaction ** d % n

        #References https://en.wikipedia.org/wiki/Digital_signature#Applications
        #https://cloud.google.com/kms/docs/digital-signatures#:~:text=A%20digital%20signature%20is%20a,a%20signature%20over%20raw%20data
        #https://www.cisa.gov/uscert/ncas/tips/ST04-018
        signature = pow(trans_hash_as_int, d, n)

        return signature

    def task_5(self, n_str: str, e_str: str) -> str:
        n = int(n_str, 16)
        e = int(e_str, 16)

        # Step 1
        p, q = self.get_factors(n)
        # Step 2
        d = self.get_private_key_from_p_q_e(p, q, e)

        return hex(d).rstrip('L')

    def task_6(self, given_public_key_n: int, given_public_key_e: int, public_key_list: list) -> int:
        # TODO: Implement this method for Task 6

        #pseudocode n = p*q
        #n // p = q
        #q = n // p
        # iterate through public key list to find public key with similar factor to the given public key
        # if i is lower than the length of the list and the given key's gcd is not equal to 1
        # calculate p
        # increment i
        #References https://factorable.net/weakkeys12.extended.pdf
        #http://www.loyalty.org/~schoen/rsa/
        #https://doc.sagemath.org/html/en/thematic_tutorials/numtheory_rsa.html
        d = 0
        i = 0

        while i < len(public_key_list):
            if math.gcd(given_public_key_n, public_key_list[i]) != 1:
                p = math.gcd(given_public_key_n, public_key_list[i])
            i += 1

        q = given_public_key_n // p
        d = self.get_private_key_from_p_q_e(p, q, given_public_key_e)

        return d

    def task_7(self, n_1_str: str, c_1_str: str, n_2_str: str, c_2_str: str, n_3_str: str, c_3_str: str) -> str:
        # TODO: Implement this method for Task 7
        n_1 = int(n_1_str, 16)
        c_1 = int(c_1_str, 16)
        n_2 = int(n_2_str, 16)
        c_2 = int(c_2_str, 16)
        n_3 = int(n_3_str, 16)
        c_3 = int(c_3_str, 16)


        #pseudocode, look for a way to find the product of n_1,n_2,n_3
        #with the product, divide with the integers (3 n's) that make up the product
        #get the modular inverse for the product and n integer
        #utilize the Chinese remainder theorem to create a message, message is product of modular inverse calculations, n calculations and c int values provided, add remaining calculations to new message, find mod product of the 3 n's 
        #x ≡ a1 (mod m1), x ≡ a2 (mod m2), ..., x ≡ ak (mod mk) 
        #References https://en.wikipedia.org/wiki/Chinese_remainder_theorem
        #https://www.flair.monash.edu.au/intranet/proceedings/icces08/paper/137.pdf
        #http://homepages.math.uic.edu/~leon/mcs425-s08/handouts/chinese_remainder.pdf
        #https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.109.1248&rep=rep1&type=pdf
        #https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
        N_1_2_3 = n_1 * n_2 * n_3
        N_1 = N_1_2_3 // n_1
        N_2 = N_1_2_3 // n_2
        N_3 = N_1_2_3 // n_3

        m_1 = self.get_modular_inverse(N_1, n_1)
        m_2 = self.get_modular_inverse(N_2, n_2)
        m_3 = self.get_modular_inverse(N_3, n_3)

        M_1_2_3 = (c_1 * N_1 * m_1 + c_2 * N_2 * m_2 + c_3 * N_3 * m_3) % N_1_2_3

        #public exponent e set to 3
        e = 3
        m = self.find_modular_inverse(M_1_2_3, e)
        # Solve for m, which is an integer value, the line below will convert it to a string:
        msg = bytes.fromhex(hex(m).rstrip('L')[2:]).decode('UTF-8')

        return msg






 