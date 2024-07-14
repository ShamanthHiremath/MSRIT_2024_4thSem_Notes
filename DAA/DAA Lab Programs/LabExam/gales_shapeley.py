def gale_shapley(men_preferences, women_preferences):
    # Number of men and women
    num_people = len(men_preferences)
    
    # Initialize all men and women as free
    free_men = list(range(num_people))
    women_partner = [-1] * num_people
    men_partner = [-1] * num_people
    # To store the index of the proposals made by each men
    proposals = [0] * num_people
    
    # While there are free men who haven't proposed to every woman
    while free_men:
        new_man = free_men.pop(0)
        woman = men_preferences[new_man][proposals[new_man]]
        proposals[new_man] += 1
        
        if women_partner[woman] == -1:  # Woman is free
            women_partner[woman] = new_man
            men_partner[new_man] = woman
        else:  # Woman is currently engaged
            current_partner = women_partner[woman]
            woman_preference = women_preferences[woman]
            # If the current partner is less preferred than the new man
            if woman_preference.index(new_man) < woman_preference.index(current_partner):
                women_partner[woman] = new_man
                men_partner[new_man] = woman
                free_men.append(current_partner)
            # If the current partner is more preferred than the new man
            else:
                free_men.append(new_man)
                
    print("Stable matchings (man -> woman):")
    for man, woman in enumerate(men_partner):
        print(f"Man {man+1} is matched to Woman {woman+1}")
        
    # return men_partner

def input_prefernces():
    n = int(input("Enter the number of people: "))
    preferences = []
    for i in range(n):
        print(f"Enter the preferences of individual {i+1}:")
        man_pref = []
        for j in range(n):
            # print(f"Enter the {j+1} preference of man {i+1} ")
            pref = int(input())
            man_pref.append(pref)
        preferences.append(man_pref)
    return preferences
    
def main():
    # Hardcoded preferences for men and women
    men_preferences = [
        [0, 1, 2],  # Man 1's preferences
        [1, 2, 0],  # Man 2's preferences
        [1, 0, 2]   # Man 3's preferences
    ]
    
    women_preferences = [
        [2, 0, 1],  # Woman 1's preferences
        [0, 1, 2],  # Woman 2's preferences
        [1, 2, 0]   # Woman 3's preferences
    ]
    
    print(input_prefernces())

    # matches = gale_shapley(men_preferences, women_preferences)
    # print("Stable matchings (man -> woman):")
    # for man, woman in enumerate(matches):
    #     print(f"Man {man+1} is matched to Woman {woman+1}")
    
    gale_shapley(men_preferences, women_preferences)
    
    

if __name__ == "__main__":
    main()