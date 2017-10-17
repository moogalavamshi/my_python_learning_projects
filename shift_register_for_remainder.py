G_X = '1101'
M_X = '1101011000'


def get_remainder_from_division(M_X=None):
    # empty list objects for shift register and XOR pattern
    s_r = []  # shift register
    s_r_xor_position = []

    # finding the length of shift register from g(x)
    for i in range(len(G_X)):
        if G_X[i] == '1':
            shift_register_length = (len(G_X) - i - 1)
            break

    print('shift_register_length-->{}'.format(shift_register_length))

    # forming the shift register along with xor gates initially
    for i in range(shift_register_length):
        s_r.append(0)
        s_r_xor_position.append(int(G_X[i + len(G_X) - shift_register_length]))

    print('shift register is --> {}'.format(s_r))
    print('shift register xor position is -->{}'.format(s_r_xor_position))

    # pushing bits to shift register from M(X) one by one
    for curr_shift_bit_from_m_x in M_X:
        print('-----cycle start with {}-----'.format(curr_shift_bit_from_m_x))

        # for passing the input from left most part in shift register to all xor gates
        input_for_xor_from_left = s_r[0]

        # for storing the value to be passed to left of shift register after performing operation on a bit of S_R
        input_for_xor_after_shift = int(curr_shift_bit_from_m_x)

        # for tracking the current bit of shift register that operation to be performed
        current_s_r_position = shift_register_length

        print('input_for_xor_from_left -->{}'.format(input_for_xor_from_left))

        # performing operations on each bit of shift register from right to left
        for i, j in zip(s_r[::-1], s_r_xor_position[::-1]):
            current_s_r_position -= 1
            print('current_s_r_position-->{}'.format(current_s_r_position))
            print("i, j-->{} {}".format(i, j))
            input_for_xor_from_left = s_r[0]
            print('input_for_xor_from_left = {},input_for_xor_after_shift = {}'.format(input_for_xor_from_left, input_for_xor_after_shift))
            print('s_r[current_s_r_position] before {}'.format(s_r[current_s_r_position]))
            if (j == 1):
                print("entered j = 1")
                s_r[current_s_r_position] = input_for_xor_from_left ^ input_for_xor_after_shift
            else:
                s_r[current_s_r_position] = input_for_xor_after_shift
            input_for_xor_after_shift = i
            print('s_r[current_s_r_position] after {}'.format(s_r[current_s_r_position]))
            print('input_for_xor_after_shift after->{}'.format(input_for_xor_after_shift))
        print(s_r)

    return s_r


rem = get_remainder_from_division(M_X)

print('rem----->{}'.format(rem))
