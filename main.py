def access():
    choice = input("Attempt to access? (y/n)\n")
    if choice == "y" or choice == "Y":
        return True
    elif choice == "n" or choice == "N":
        return False
    while choice not in "yYnN":
        if choice == "y" or choice == "Y":
            return True
        elif choice == "n" or choice == "N":
            return False
        else:
            print("Please enter y or n.")
            choice = input("Attempt to access? (y/n)\n")


def menu_a():
    print()
    print("i - General Information")
    print("ii - Experimental Code")
    print("iii - Preliminary Experiments")
    number = input("Access to Archive: ")
    print()
    if number == "i":
        print("[Subject No.166: General Information]")
        print("Subject number: No.166")
        print("Subject name: Mimetic butterfly\n")
        print("No.166 has two stages.")
        print("  The first stage is a white rice-sized insect egg, about 1 cm in diameter, with a smooth but not \n"
              "metallic surface. The second stage is present only in the host. No.166 hatches and grows at different\n"
              "lengths depending on the host species. Without a host, No.166 would hatch into a butterfly with black-\n"
              "brown body, blue wings and yellow-white markings.")
        print("  The subject matures spontaneously upon entry into the host and controls the host's nervous system\n"
              "through a specific secretion. An fmri scan of the infected individual's brain reveals a significant\n"
              "increase in amygdala activity. It can be inferred that at this stage the infected individual is\n"
              "still conscious, but its neural impulses cannot reach the relevant effector organs. After the\n"
              "incubation period and the incubation period, the mature adult can completely replace the brain of\n"
              "the infected individual and mimic its previous behaviors, allowing the subject to fully integrate\n"
              "into the colony.")
        print("  The subject was not found to be self-subjective but seems to follow instincts only. No significant\n"
              "differences were found between individuals.")
    elif number == "ii":
        print("[Subject No.166: Experimental Code]")
        print("1. Laboratory personnel should take full protective measures when in contact with No.166, including\n"
              "   but not limited to respiratory endocyclic system, latex gloves, and enclosed goggles.")
        print("2. Experimenters should have no more than 2 hours of continuous direct contact with No.166 and should\n"
              "   be isolated for more than 48 hours after exposure and undergo fmri brain scans to ensure that they\n"
              "   are not parasitized.")
        print("3. Laboratory personnel are subject to UV disinfection and inspection before and after entering and\n"
              "   leaving the laboratory to prevent the release of experimental subjects.")
        print("4. Animals parasitized by no.166 need to be monitored 24/7 to prevent escape behavior.")
        print("5. Experimental subjects and contents are to be kept strictly confidential. Experimental materials\n"
              "   must not be taken out of the laboratory.")
    elif number == "iii":
        print("[Subject No.166: Preliminary Experiments]")
        menu_a_sub()
    else:
        print("File does not exist. Please re-enter.")
        menu_a()


def menu_a_sub():
    print("A. Preliminary Experiments - Stage One")
    print("B. Preliminary Experiments - Stage Two")
    option = input("Access to Archive: ")
    while option not in "aAbB":
        print("Invalid Input. Please Re-enter.")
        option = input("Access to Archive: ")
    if option == "A" or option == "a":
        print("\nStage One - Insect & Animal Experiments\n")
        print("[Subject: Swarming insects - bee]")
        print("Observation: Host death within 10 hours")
        print("Inference: Host is too small. Unable to provide the energy needed to hatch No.166.")
        print("Notes: Subsequent test targets expanded to mammals.")
        print()
        print("[Subject: Rodents - rat (live)]")
        print("Observation: Live host showed transient convulsions 24 hours after parasitization, then no abnormal\n"
              "           movement; all indicators were normal except for increased response to brain activity; no\n"
              "           abnormalities in the population.")
        print("Inference: No.166 exhibited a strong mimetic ability and was able to replace the host for normal\n"
              "           social and survival activities.")
        print()
        print("[Subject: Rodents - rat (dead)]")
        print("Observation: The inanimate host showed weak vital signs after 30 hours of parasitization; increased\n"
              "             mobility and disorganized movement after 43 hours. All indicators were normal except\n"
              "             for increased brain activity response. The population was well accepted after contact\n"
              "             and returned to normal behavior within four hours.")
        print("Inference: No.166 incubation conditions were not related to host vital signs. However, when the host\n"
              "           was dead, its mimicry behavior was not inherited from the original host, but from other\n"
              "           individuals within the colony.")
        print("Notes: The results of No.166 performance under dead host conditions may point to its potential\n"
              "      value in the medical field. Subsequent experiments should be conducted in this direction.")
        print()
        print("[Subject: Primate - gibbon (dead)]")
        print("Observation: The inanimate host showed weak vital signs after 36 hours of parasitism and increased\n"
              "             mobility and disorganized movement after 50 hours. All indicators were normal except\n"
              "             for a weak response to brain activity. The population was well accepted after contact\n"
              "             and returned to normal behavior within four hours.")
        print("Inference: No.166 incubation time was proportional to the size of the host. Its mimicry ability did\n"
              "           not show significant differences between host races.")
        print("Notes: Further evidence of the value of No.166 in the medical field.")
        print("Notes: How does it resend neural signals to make the body work when the host has died?   - ██████")
    elif option == "B" or option == "b":
        print("\nStage Two - Human Experiments\n")
        print("Access Permission Required: Primary Researchers or above")
        print("Verifying access permission...\nIdentity confirmed.\nAccess permission approved.\n")
        print("[Subject: Adult Male (cadaver)]")
        print("Observation: Observation: The inanimate host showed weak vital signs after 38 hours of parasitization\n"
              "             and increased mobility and disorganized movement after 52 hours. All indicators were\n"
              "             normal except for increased brain activity response.")
        print("Notes: The experimenters did not have direct contact with the host for the time being.")
        print()
        print("[Subject: Adult Male (paralyzed)]")
        print("Access Permission Required: Upper Level Approval")
        print("Verifying access permission...\nIdentity confirmed.\nAccess denied.\n")
        print("Auto-exit from current page...")


def menu_b():
    print()
    print("Case 0 - Application in 2035")
    print("Case 1 - Application in 2038")
    print("Case 2 - Application in Jan 2040")
    print("Case 3 - Application in Aug 2040")
    print("Case 4 - Malignant Event in Feb 2041")
    print("Case 5 - Application in Jul 2041")
    num = input("Access to Case: ")
    print()
    if num == "0":
        print("[Mimetic Butterfly: 2035 #0 Test]")
        print("  Access Permission Required: Primary Researchers or above")
        print("  Verifying access permission...\n  Identity confirmed.\n  Access permission approved.\n")
        print("Type: Private Unauthorized Application, Without Formal Process Review")
        print("  Primary researcher ████ illegally took No.166 experimental sample and implanted it in his daughter\n"
              "who died in a car accident. His neighbor reported the case to the general police, as the daughter ███\n"
              "reappeared in the house six months after the car accident. The case was classified as a misreport and\n"
              "the reporting person was pacified and silenced.")
    elif num == "1":
        print("[Mimetic Butterfly: 2038 #1 Application]")
        print("Type: Experimental Application, Reviewed by Routine Procedures")
        print("  Renowned theoretical physicist ████ was dying of bone cancer. After a tentative docking with the\n"
              "researcher, the subject himself applied and signed a consent form to accept the No.166 implantation\n"
              "experiment. Since the subject was implanted while the host was still conscious, No.166 exhibited\n"
              "identical behavior to that of A in health, including daily routines and academic activities.\n"
              "Follow-up observations showed that No.166's mimicry ability was not limited by academic professional\n"
              "requirements.")
    elif num == "2":
        print("[Mimetic Butterfly: 2040 #2 Application]")
        print("Type: Experimental Application, Reviewed by Routine Procedures")
        print()
        print("Appendix: [Extensive Application Proposal]")
        print("  Deliberation Result: Proposal Rejected")
        print("  There is an 88% probability that rushing to mass propagation and application at this stage will\n"
              "cause serious public panic. The rejection does not negate the full scale application, but rather\n"
              "specifies the application of No. 166 in areas of strong need, including but not limited to medical,\n"
              "scientific, and public safety issues.")
    elif num == "3":
        print("[Mimetic Butterfly: 2040 #3 Application]")
        print("  Access Permission Required: Primary Researchers or above")
        print("  Verifying access permission...\n  Identity confirmed.\n  Access permission approved.\n")
        print("Type: Private Unauthorized Application, Without Formal Process Review")
        print("  ████. the head of ████ was involved in ███ malignant incident, to shirk responsibility he concealed\n"
              "the number of accidental deaths and coerced Primary Researcher ███ to bring out the experimental\n"
              "sample of No.166 from the laboratory and implanted No.166 into the corpses, thus making it parasitic\n"
              "in the accident victims and \"living\" with the original identity of the victims. The accident has\n"
              "constituted a serious consequence. Both ███ and researcher ███ have been arrested. For the community's\n"
              "safety, this incident was kept confidential from the public, but remaining potential risk factors\n"
              "still require long-term surveillance.")
    elif num == "4":
        print("Mimetic Butterfly: 2041 #4 Malignant Event]")
        print("  Access Permission Required: Primary Researchers or above")
        print("  Verifying access permission...\n  Identity confirmed.\n  Access permission approved.\n")
        print("  This case was the main trigger for the discovery of Case #3. 38-year-old housewife ███ murdered her\n"
              "husband at home as she suspected that he was not her husband six months after incident ███. After\n"
              "discovering the traces of No.166 in her husband's brain, ███ lost her temper and killed her children,\n"
              "who also experienced incident ███. After the murder, ███ went to the nearest police station and turned\n"
              "herself in.")
        print("  According to forensic examination, ███'s husband was indeed the victim of No.166 in incident ███,\n"
              "but her son and daughter were not parasitized. Both suffered only minor injuries in the accident and\n"
              "would have returned to their normal lives after brief treatments in the hospital.")
        print("\nAppendix: [Excerpts From ███'s Diary]")
        print('Aug 13, 2040: "Thank goodness Darling and the kids made it back alive! There is no official\n'
              '              announcement about what happened at the scene, but terrible things must have happened.\n'
              '              It\'s a miracle that only the kids were slightly injured! Oh thank God!"')
        print('Sep 5, 2040: "The kids have been a bit quiet lately, probably because they are scared.\n'
              '             Thankfully my husband is as supportive as ever and I hope the kids are okay."')
        print('Oct 3, 2040: "I don\'t know. There\'s always an unexplainable sense of dissonance in the house.\n'
              '             Maybe they haven\'t gotten over the accident yet? I always have the illusion that\n'
              '             someone is watching me. Lately I\'ve been waking up in the middle of the night in a\n'
              '             cold sweat. Or maybe it\'s me? I don\'t know."')
        print('Nov 31, 2040: "Something\'s wrong. I know."')
        print('Jan 1, 2041: "Am I crazy? My husband is not my husband! He looks like him, he sounds like him, he\n'
              '             writes, he reads, he eats like him. But why do I feel that he has changed. Or maybe\n'
              '             it\'s because he hasn\'t changed, he hasn\'t changed at all that makes me feel creepy.\n'
              '             I have to find someone to ask."')
        print('Jan 7, 2041: "They all say there\'s nothing wrong. The one with the problem is me? I do have a\n'
              '             problem. The kids look at me differently, like I\'m doing something hysterical. But\n'
              '             the husband, he hasn\'t changed. That look, that look!"')
        print('Feb 1, 2041: "I have to solve the problem myself."')
    elif num == "5":
        print("[Mimetic Butterfly: 2041 #5 Application]")
        print("  Access Permission Required: Upper Level Approval")
        print("  Verifying access permission...\nIdentity confirmed.\nAccess denied.\n")
        print("Auto-exit from current page...")
    else:
        print("File does not exist. Please re-enter.")
        menu_b()


def menu_c():
    print()
    print("A: Program Evaluation")
    print("B: Application Plans")
    choice = input("Access to: ")
    while choice not in "aAbB":
        print("Invalid Input. Please Re-enter.")
        choice = input("Access to: ")
    if choice == "a" or choice == "A":
        print("\n[Subject No.166: Analysis Report]")
        print("  (File deleted)")
        print("  According to the personnel investigation, the analyst has a distant relative involved in Case 3,\n"
              "March 2040. Although he claimed to have no knowledge of the situation, it cannot be ruled out that\n"
              "there are potential subjective assumptions in his analysis report.")
        print("  This report is hereby nullified.")
        print("\nAppendix: [Interrogation of ███·█·██]")
        print("  \"How are you guys totally oblivious to how creepy these bugs are!\"")
        print("  \"The friends and family you thought might be just an empty human skin! They' re just nasty bugs\n"
              "playing with dead bodies underneath!\"")
        print("""  "You can't impris*gJt$EpCb$K^@&W9Wige(mXEuwg;JVfMzD'Y{ojh%%FvE;=L5F-S'~>C`jtFewq>L?i?6@vkxUx&3
AM2AH#;Lc~@Cd$K%XuPgs;X&$C+Qb{H-B:mi)pCC]]pBTW+>W?V,@mq+:n=eF!eA7ovrSbtP`(dsbCkV-D$]4G@#7'D/~VZgc
6*x/;8-8/$U++Ww$mERm^_MyTq6U5^+J4>p/:PgMNAx$ExVXzo}$FCCUM$!zkAf""")
        print("  (Data Corrupted)\n  (Please contact HR and technical departments for file repair.)")
    elif choice == "b" or choice == "B":
        print("\n[Subject No.166: Application Plan]")
        print("                                                                      - Updated in September 2033")
        print("  The experiment showed that No.166 demonstrates great adaptability in mimicking the behavior of the\n"
              "host. The researchers deduced that by studying its mechanism of controlling neural signals in the\n"
              "host's physical body, a great breakthrough could be made in the field of treating brain diseases and\n"
              "neurological diseases. Its mimetic ability also possesses potential value in the field of artificial\n"
              "intelligence development. Further research should be conducted on mammals and primates to explore its\n"
              "potential applications.")
        print("\n[Subject No.166: Application Plan]")
        print("                                                                        - Updated in January 2040")
        print("  The value of No.166 in practical terms is beyond expectation. Its use in the medical field still\n"
              "need to be explored and experimented with for long-term applications. Predictably, the implementation\n"
              "of No.166 in Bioethics is still strongly controversial, but the application value of the experimental\n"
              "subjects far exceeds the controversy itself. At this stage, the research direction should be\n"
              "maintained, and small-scale application experiments should be conducted.")
        print("Appendix: [███·██ Instructions]")
        print("  No.166's inheritance of the live host's behavior pattern and its ability of manipulating the nervous\n"
              "system can even achieve the miracle of \"life extension\" and \"resurrection from the dead\". This is a\n"
              "goal that cannot be accomplished by any means with our science and technology in the current era.\n"
              "Despite its controversial nature, we cannot give up on this. No.166 will surely be the inevitable step\n"
              "towards the next level of human life, and will be our hope for the future.")
        print("                                                                                         - ███·██")
        print("Appendix: [No.166 Application Plan Proposal]")
        print("  Access Permission Required: Upper Level Approval")
        print("  Verifying access permission...\n  Identity confirmed.\n  Access denied.")
        print("\n[Subject No.166: Application Plan]")
        print("                                                                           - Updated in June 2040")
        print("  Access Permission Required: Upper Level Approval")
        print("  Verifying access permission...\n  Identity confirmed.\n  Access denied.")
        print("Appendix: [Program Personnel List]")
        print("  Access Permission Required: Upper Level Approval")
        print("  Verifying access permission...\n  Identity confirmed.\n  Access denied.\n")
        print("Auto-exit from current page...")


def menu():
    print()
    print("A: [Basic Archives]")
    print("B: [Related Cases Records]")
    print("C: [Evaluation and Planning Programs]")
    print("D: Exit")
    option = input()
    if option == "a" or option == "A":
        menu_a()
    elif option == "b" or option == "B":
        menu_b()
    elif option == "c" or option == "C":
        menu_c()
    elif option == "d" or option == "D":
        print("Logging out of the file system...")
        print("Exit successfully.")
        exit()
    else:
        print("Invalid input.\nPlease re-enter.")
        menu()
    back = aftermenu()
    if back:
        menu()
    else:
        print("Logging out of the file system...")
        print("Exit successfully.")
        exit()


def aftermenu():
    print("\nRetrieval completed")
    user_input = input("Return to directory?(y/n)\n")
    while user_input not in "yYnN":
        print("Invalid input.\nPlease re-enter.")
        user_input = input("Return to directory?(y/n)\n")
    if user_input == "y" or user_input == "Y":
        return True
    elif user_input == "n" or user_input == "N":
        return False


print("[Subject No.166: Mimetic Butterfly]")
print("This archive records the information about subject No.166 and its related cases.\n")
print("ACCESS BY UNAUTHORIZED PERSONNEL IS STRICTLY PROHIBITED\nPERPETRATORS WILL BE TRACKED, LOCATED, AND DETAINED\n")
result = access()
if result:
    print("Access Permission Required: Secondary Researchers or above")
    print("Verifying access permission...\nIdentity confirmed.\nAccess permission approved.")
    menu()
    print("\nRetrieval completed")
    user = input("Return to directory?(y/n)\n")
    while user not in "yYnN":
        print("Invalid input.\nPlease re-enter.")
        user = input("Return to directory?(y/n)\n")
    if user == "y" or user == "Y":
        menu()
    elif user == "n" or user == "N":
        print("Logging out of the file system...")
        print("Exit successfully.")
else:
    print("Logging out of the file system...")
    print("Exit successfully.")
