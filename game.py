import random
import time

# It looks like I simply put different peaces of code to different classes :D
# I really have no idea about how to use them in this case...


class Squads:
    ar = 'archer'
    kn = 'knight'
    wi = 'wizard'

    num_for_ar = random.randint(15, 47)
    num_for_kn = random.randint(15, 47)
    num_for_wi = (100 - (num_for_ar + num_for_kn))

    comps_army = [(ar, num_for_ar), (kn, num_for_kn), (wi, num_for_wi)]
    h = random.shuffle(comps_army)

    ordered_c_a = {
        '1': comps_army[0],
        '2': comps_army[1],
        '3': comps_army[2]
    }

    def or_co_arm(self):
        for v, j in sorted(self.ordered_c_a.items()):
            return v + ')', j

    comprefig = sorted(ordered_c_a.items())
    c_fig1, c_fig2, c_fig3 = comprefig
    c_f_new1, c_f_new2, c_f_new3 = c_fig1[1], c_fig2[1], c_fig3[1]
    comp_num_figh = [c_f_new1[1], c_f_new2[1], c_f_new3[1]]


    print('Please choose the number of soldiers for each squad.',
          '\nThe number of all soldiers in your army should bo 100:')
    user_ar = int(input('archer: '))
    user_kn = int(input('knight: '))
    user_wi = int(input('wizard: '))
    time.sleep(.5)
    if user_ar + user_kn + user_wi == 100:
        pass
    elif user_ar + user_kn + user_wi > 100:
        print('Hey, your army seems to be too big! It should be equal right to 100 soldiers!')
        exit()
    elif user_ar + user_kn + user_wi < 100:
        print('Hey, your army seems to be too small! It should be equal right to 100 soldiers!')
        exit()

    print('Now please set the order in which your squads should enter the battle:')
    sqd_num_ar = int(input('archer: '))
    sqd_num_kn = int(input('knight: '))
    sqd_num_wi = int(input('wizard: '))
    time.sleep(.5)
    user_constant = [sqd_num_ar, sqd_num_kn, sqd_num_wi]

    checker = [1, 2, 3]
    checking = sorted([sqd_num_ar, sqd_num_kn, sqd_num_wi])

    def check(self):
        if self.checking == self.checker:
            pass
        else:
            return "Something is wrong with the order you've set...", exit()

    def user_sort(self):
        if Squads.sqd_num_ar == 1:
            print(Squads.sqd_num_ar, ') ' + Squads.ar + ' <-- Fighting first!')
            if Squads.sqd_num_kn == 2:
                print(Squads.sqd_num_kn, ') ' + Squads.kn)
                if Squads.sqd_num_wi == 3:
                    print(Squads.sqd_num_wi, ') ' + Squads.wi)
            elif Squads.sqd_num_wi == 2:
                print(Squads.sqd_num_wi, ') ' + Squads.wi)
                if Squads.sqd_num_kn == 3:
                    print(Squads.sqd_num_kn, ') ' + Squads.kn)
        elif Squads.sqd_num_kn == 1:
            print(Squads.sqd_num_kn, ') ' + Squads.kn + ' <-- Fighting first!')
            if Squads.sqd_num_ar == 2:
                print(Squads.sqd_num_ar, ') ' + Squads.ar)
                if Squads.sqd_num_wi == 3:
                    print(Squads.sqd_num_wi, ') ' + Squads.wi)
            elif Squads.sqd_num_wi == 2:
                print(Squads.sqd_num_wi, ') ' + Squads.wi)
                if Squads.sqd_num_ar == 3:
                    print(Squads.sqd_num_ar, ') ' + Squads.ar)
        elif Squads.sqd_num_wi == 1:
            print(Squads.sqd_num_wi, ') ' + Squads.wi + ' <-- Fighting first!')
            if Squads.sqd_num_kn == 2:
                print(Squads.sqd_num_kn, ') ' + Squads.kn)
                if Squads.sqd_num_ar == 3:
                    print(Squads.sqd_num_ar, ') ' + Squads.ar)
            elif Squads.sqd_num_ar == 2:
                print(Squads.sqd_num_ar, ') ' + Squads.ar)
                if Squads.sqd_num_kn == 3:
                    print(Squads.sqd_num_kn, ') ' + Squads.kn)

    similazer1 = [1, 2, 3]
    similazer2 = [3, 2, 1]
    similazer3 = [1, 3, 2]
    similazer4 = [2, 3, 1]
    similazer5 = [2, 1, 3]
    similazer6 = [3, 1, 2]

    def user_num_figh(self):
        if Squads.user_constant == Squads.similazer1:
            Squads.user_num_figh = [Squads.user_ar, Squads.user_kn, Squads.user_wi]
            return Squads.user_num_figh
        elif Squads.user_constant == Squads.similazer2:
            Squads.user_num_figh = [Squads.user_wi, Squads.user_kn, Squads.user_ar]
            return Squads.user_num_figh
        elif Squads.user_constant == Squads.similazer3:
            Squads.user_num_figh = [Squads.user_ar, Squads.user_wi, Squads.user_kn]
            return Squads.user_num_figh
        elif Squads.user_constant == Squads.similazer4:
            Squads.user_num_figh = [Squads.user_wi, Squads.user_ar, Squads.user_kn]
            return Squads.user_num_figh
        elif Squads.user_constant == Squads.similazer5:
            Squads.user_num_figh = [Squads.user_kn, Squads.user_ar, Squads.user_wi]
            return Squads.user_num_figh
        elif Squads.user_constant == Squads.similazer6:
            Squads.user_num_figh = [Squads.user_wi, Squads.user_ar, Squads.user_kn]
            return Squads.user_num_figh
        else:
            return 'strange. very strange'


# What about 'righter' variable(in Fight class)... If you noticed the computer counts the results of each clash in a very strange way...
# I've written multipliers for each fighting number (I mean squad) in every possible case!
# But this program (let it burn with blue flame, I have no nerves for it anymore) does not want to count the results
# correctly!! I've checked it 3000000 times!...((
# So I thought that the reason is this: on 3rd, 4th, 5th etc steps two squads were equal to the same number (0).
# And I've created the variable 'righter' and connected my checking to it.
# But... It seems that I get the same result :\
# Then I understood that  that's not the reason, because counters (i and k) are different every time.
# But what's the matter then? I'm very disappointed with it.


class Fight(Squads):
    def __init__(self):
        super().__init__()

    def battle(self):
        i = 0
        k = 0
        r = 0
        righter = ['killed', 'dead', 'murdered', 'finished', 'erased', 'done', 'slayed']  # Phahahah :D What a nice
        while i <= len(self.comp_num_figh) - 1 or k <= len(self.user_num_figh) - 1:       # variety of synonyms...
            time.sleep(.5)
            if self.comp_num_figh[i] == self.num_for_ar:
                if self.user_num_figh[k] == self.user_ar:
                    mj = 1
                    mk = 1
                elif self.user_num_figh[k] == self.user_kn:
                    mj = 2
                    mk = 0.5
                elif self.user_num_figh[k] == self.user_wi:
                    mj = 0.5
                    mk = 2
            elif self.comp_num_figh[i] == self.num_for_kn:
                if self.user_num_figh[k] == self.user_ar:
                    mj = 0.5
                    mk = 2
                elif self.user_num_figh[k] == self.user_kn:
                    mj = 1
                    mk = 1
                elif self.user_num_figh[k] == self.user_wi:
                    mj = 2
                    mk = 0.5
            elif self.comp_num_figh[i] == self.num_for_wi:
                if self.user_num_figh[k] == self.user_ar:
                    mj = 2
                    mk = 0.5
                elif self.user_num_figh[k] == self.user_kn:
                    mj = 0.5
                    mk = 2
                elif self.user_num_figh[k] == self.user_wi:
                    mj = 1
                    mk = 1
            form = int((self.comp_num_figh[i] * mj) - (self.user_num_figh[k] * mk))
            if form < 0:
                self.user_num_figh[k] = int(self.user_num_figh[k] - (self.comp_num_figh[i] * mj))
                self.comp_num_figh[i] = righter[r]
                print('Your army:    ', self.user_num_figh)
                print("Rival's army: ", self.comp_num_figh)
                print('')
                if type(self.user_num_figh[2]) != int and type(self.comp_num_figh[2]) != int:  # == str -- already tried
                    return '....... Nobody won .......'                                       # it works without classes
                elif type(self.comp_num_figh[2]) != int:
                    return '----*** You WON! Congrats! ***----'
                elif type(self.user_num_figh[2]) != int:
                    return '--- You lost... Good luck next time! ---'
                i += 1
                r += 1
            elif form > 0:
                self.comp_num_figh[i] = int(self.comp_num_figh[i] - (self.user_num_figh[k] * mk))
                self.user_num_figh[k] = righter[r]
                print('Your army:    ', self.user_num_figh)
                print("Rival's army: ", self.comp_num_figh)
                print('')
                if type(self.user_num_figh[2]) != int and type(self.comp_num_figh[2]) != int:
                    return '....... Nobody won .......'
                elif type(self.comp_num_figh[2]) != int:
                    return '----*** You WON! Congrats! ***----'
                elif type(self.user_num_figh[2]) != int:
                    return '--- You lost... Good luck next time! ---'
                k += 1
                r += 1
            elif form == 0:
                self.comp_num_figh[i] = righter[r]
                self.user_num_figh[k] = righter[r]
                print('Your army:    ', self.user_num_figh)
                print("Rival's army: ", self.comp_num_figh)
                print('')
                if type(self.user_num_figh[2]) != int and type(self.comp_num_figh[2]) != int:
                    return '....... Nobody won .......'
                elif type(self.comp_num_figh[2]) != int:
                    return '----*** You WON! Congrats! ***----'
                elif type(self.user_num_figh[2]) != int:
                    return '--- You lost... Good luck next time! ---'
                i += 1
                k += 1
                r += 1


squads = Squads()
fight = Fight()

squads.check()
squads.user_sort()
time.sleep(.5)

print("Ok, and your rival's army is...")
time.sleep(.5)
squads.or_co_arm()
time.sleep(.5)

print('')
print('Now... The Great Battle is beginning!')
time.sleep(.5)

squads.user_num_figh()
print('Your army:    ', squads.user_num_figh)
time.sleep(.5)

print("Rival's army: ", squads.comp_num_figh)
print('')

time.sleep(.5)
fight.battle()
