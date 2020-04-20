def is_partial_permutation(template, test):
    if len(template) != len(test) or template[0] != test[0]:
        return False
    else:
        template_dict = {}
        test_dict = {}

        # Check if the words have the same letters
        for index in range(1, len(template)):
            if template[index] not in template_dict:
                template_dict[template[index]] = 1
            else:
                template_dict[template[index]] += 1

            if test[index] not in test_dict:
                test_dict[test[index]] = 1
            else:
                test_dict[test[index]] += 1

        if template_dict != test_dict:
            return False

        if len(template) >= 3:
            change_possibility = int(2/3 * len(template))

            for index in range(1, len(template)):
                if template[index] != test[index]:
                    if change_possibility > 0:
                        change_possibility -= 1
                    else:
                        return False

        return True


template_input, test_input = input().replace(" ", "").split(",")

print(is_partial_permutation(template_input, test_input))
