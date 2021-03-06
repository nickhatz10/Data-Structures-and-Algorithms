# -*- coding: utf-8 -*-
"""Needleman_Wunsch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FvsZUgAeLs9rD1OdT7Fz82LP5lv-u_6q
"""

blosum50 = {'A': {'A': 5.0, 'C': -1.0, 'D': -2.0, 'E': -1.0, 'F': -3.0, 'G': 0.0, 'H': -2.0, 'I': -1.0, 'K': -1.0, 'L': -2.0, 'M': -1.0, 'N': -1.0, 'P': -1.0, 'Q': -1.0, 'R': -2.0, 'S': 1.0, 'T': 0.0, 'V': 0.0, 'W': -3.0, 'Y': -2.0},
'C': {'A': -1.0, 'C': 13.0, 'D': -4.0, 'E': -3.0, 'F': -2.0, 'G': -3.0, 'H': -3.0, 'I': -2.0, 'K': -3.0, 'L': -2.0, 'M': -2.0, 'N': -2.0, 'P': -4.0, 'Q': -3.0, 'R': -4.0, 'S': -1.0, 'T': -1.0, 'V': -1.0, 'W': -5.0, 'Y': -3.0},
'D': {'A': -2.0, 'C': -4.0, 'D': 8.0, 'E': 2.0, 'F': -5.0, 'G': -1.0, 'H': -1.0, 'I': -4.0, 'K': -1.0, 'L': -4.0, 'M': -4.0, 'N': 2.0, 'P': -1.0, 'Q': 0.0, 'R': -2.0, 'S': 0.0, 'T': -1.0, 'V': -4.0, 'W': -5.0, 'Y': -3.0},
'E': {'A': -1.0, 'C': -3.0, 'D': 2.0, 'E': 6.0, 'F': -3.0, 'G': -3.0, 'H': 0.0, 'I': -4.0, 'K': 1.0, 'L': -3.0, 'M': -2.0, 'N': 0.0, 'P': -1.0, 'Q': 2.0, 'R': 0.0, 'S': -1.0, 'T': -1.0, 'V': -3.0, 'W': -3.0, 'Y': -2.0},
'F': {'A': -3.0, 'C': -2.0, 'D': -5.0, 'E': -3.0, 'F': 8.0, 'G': -4.0, 'H': -1.0, 'I': 0.0, 'K': -4.0, 'L': 1.0, 'M': 0.0, 'N': -4.0, 'P': -4.0, 'Q': -4.0, 'R': -3.0, 'S': -3.0, 'T': -2.0, 'V': -1.0, 'W': 1.0, 'Y': 4.0},
'G': {'A': 0.0, 'C': -3.0, 'D': -1.0, 'E': -3.0, 'F': -4.0, 'G': 8.0, 'H': -2.0, 'I': -4.0, 'K': -2.0, 'L': -4.0, 'M': -3.0, 'N': 0.0, 'P': -2.0, 'Q': -2.0, 'R': -3.0, 'S': 0.0, 'T': -2.0, 'V': -4.0, 'W': -3.0, 'Y': -3.0},
'H': {'A': -2.0, 'C': -3.0, 'D': -1.0, 'E': 0.0, 'F': -1.0, 'G': -2.0, 'H': 10.0, 'I': -4.0, 'K': 0.0, 'L': -3.0, 'M': -1.0, 'N': 1.0, 'P': -2.0, 'Q': 1.0, 'R': 0.0, 'S': -1.0, 'T': -2.0, 'V': -4.0, 'W': -3.0, 'Y': 2.0},
'I': {'A': -1.0, 'C': -2.0, 'D': -4.0, 'E': -4.0, 'F': 0.0, 'G': -4.0, 'H': -4.0, 'I': 5.0, 'K': -3.0, 'L': 2.0, 'M': 2.0, 'N': -3.0, 'P': -3.0, 'Q': -3.0, 'R': -4.0, 'S': -3.0, 'T': -1.0, 'V': 4.0, 'W': -3.0, 'Y': -1.0},
'K': {'A': -1.0, 'C': -3.0, 'D': -1.0, 'E': 1.0, 'F': -4.0, 'G': -2.0, 'H': 0.0, 'I': -3.0, 'K': 6.0, 'L': -3.0, 'M': -2.0, 'N': 0.0, 'P': -1.0, 'Q': 2.0, 'R': 3.0, 'S': 0.0, 'T': -1.0, 'V': -3.0, 'W': -3.0, 'Y': -2.0},
'L': {'A': -2.0, 'C': -2.0, 'D': -4.0, 'E': -3.0, 'F': 1.0, 'G': -4.0, 'H': -3.0, 'I': 2.0, 'K': -3.0, 'L': 5.0, 'M': 3.0, 'N': -4.0, 'P': -4.0, 'Q': -2.0, 'R': -3.0, 'S': -3.0, 'T': -1.0, 'V': 1.0, 'W': -2.0, 'Y': -1.0},
'M': {'A': -1.0, 'C': -2.0, 'D': -4.0, 'E': -2.0, 'F': 0.0, 'G': -3.0, 'H': -1.0, 'I': 2.0, 'K': -2.0, 'L': 3.0, 'M': 7.0, 'N': -2.0, 'P': -3.0, 'Q': 0.0, 'R': -2.0, 'S': -2.0, 'T': -1.0, 'V': 1.0, 'W': -1.0, 'Y': 0.0},
'N': {'A': -1.0, 'C': -2.0, 'D': 2.0, 'E': 0.0, 'F': -4.0, 'G': 0.0, 'H': 1.0, 'I': -3.0, 'K': 0.0, 'L': -4.0, 'M': -2.0, 'N': 7.0, 'P': -2.0, 'Q': 0.0, 'R': -1.0, 'S': 1.0, 'T': 0.0, 'V': -3.0, 'W': -4.0, 'Y': -2.0},
'P': {'A': -1.0, 'C': -4.0, 'D': -1.0, 'E': -1.0, 'F': -4.0, 'G': -2.0, 'H': -2.0, 'I': -3.0, 'K': -1.0, 'L': -4.0, 'M': -3.0, 'N': -2.0, 'P': 10.0, 'Q': -1.0, 'R': -3.0, 'S': -1.0, 'T': -1.0, 'V': -3.0, 'W': -4.0, 'Y': -3.0},
'Q': {'A': -1.0, 'C': -3.0, 'D': 0.0, 'E': 2.0, 'F': -4.0, 'G': -2.0, 'H': 1.0, 'I': -3.0, 'K': 2.0, 'L': -2.0, 'M': 0.0, 'N': 0.0, 'P': -1.0, 'Q': 7.0, 'R': 1.0, 'S': 0.0, 'T': -1.0, 'V': -3.0, 'W': -1.0, 'Y': -1.0},
'R': {'A': -2.0, 'C': -4.0, 'D': -2.0, 'E': 0.0, 'F': -3.0, 'G': -3.0, 'H': 0.0, 'I': -4.0, 'K': 3.0, 'L': -3.0, 'M': -2.0, 'N': -1.0, 'P': -3.0, 'Q': 1.0, 'R': 7.0, 'S': -1.0, 'T': -1.0, 'V': -3.0, 'W': -3.0, 'Y': -1.0},
'S': {'A': 1.0, 'C': -1.0, 'D': 0.0, 'E': -1.0, 'F': -3.0, 'G': 0.0, 'H': -1.0, 'I': -3.0, 'K': 0.0, 'L': -3.0, 'M': -2.0, 'N': 1.0, 'P': -1.0, 'Q': 0.0, 'R': -1.0, 'S': 5.0, 'T': 2.0, 'V': -2.0, 'W': -4.0, 'Y': -2.0},
'T': {'A': 0.0, 'C': -1.0, 'D': -1.0, 'E': -1.0, 'F': -2.0, 'G': -2.0, 'H': -2.0, 'I': -1.0, 'K': -1.0, 'L': -1.0, 'M': -1.0, 'N': 0.0, 'P': -1.0, 'Q': -1.0, 'R': -1.0, 'S': 2.0, 'T': 5.0, 'V': 0.0, 'W': -3.0, 'Y': -2.0},
'V': {'A': 0.0, 'C': -1.0, 'D': -4.0, 'E': -3.0, 'F': -1.0, 'G': -4.0, 'H': -4.0, 'I': 4.0, 'K': -3.0, 'L': 1.0, 'M': 1.0, 'N': -3.0, 'P': -3.0, 'Q': -3.0, 'R': -3.0, 'S': -2.0, 'T': 0.0, 'V': 5.0, 'W': -3.0, 'Y': -1.0},
'W': {'A': -3.0, 'C': -5.0, 'D': -5.0, 'E': -3.0, 'F': 1.0, 'G': -3.0, 'H': -3.0, 'I': -3.0, 'K': -3.0, 'L': -2.0, 'M': -1.0, 'N': -4.0, 'P': -4.0, 'Q': -1.0, 'R': -3.0, 'S': -4.0, 'T': -3.0, 'V': -3.0, 'W': 15.0, 'Y': 2.0},
'Y': {'A': -2.0, 'C': -3.0, 'D': -3.0, 'E': -2.0, 'F': 4.0, 'G': -3.0, 'H': 2.0, 'I': -1.0, 'K': -2.0, 'L': -1.0, 'M': 0.0, 'N': -2.0, 'P': -3.0, 'Q': -1.0, 'R': -1.0, 'S': -2.0, 'T': -2.0, 'V': -1.0, 'W': 2.0, 'Y': 8.0}}

# creates a class with functions to allow us to find the global alignment and optimal global alignment score
# between two strings
class needleman_wunsch_algo():

  # initiate important parameters for the needleman_wunsch algorithm to work
  def __init__(self, seq1, seq2, gap_pen, blosum_mat):
    self.seq1 = seq1
    self.seq2 = seq2
    self.gap_pen = gap_pen
    self.blosum_mat = blosum_mat

  # gets the initial matrix using numpy zeros function and the gap penalty (for the first column and first row)
  def get_matrix(self):

    # gets the length of each sequence and adds 1 to each since the matrix will be 1 bigger than the length
    n = len(self.seq1) + 1
    m = len(self.seq2) + 1

    # uses numpy to create a matrix of all zeros of the desired size
    import numpy
    mat = numpy.zeros((n,m))

    #fills in the gap penalty on the first row
    for i in range(1, m):
      mat[0][i] = self.gap_pen * i

    # fills in the gap penalty on the first column
    for j in range(1, n):
      mat[j][0] = self.gap_pen * j

    # returns the initiliazed matrix
    return mat
  
  # returns a dictionary of the traceback (either left, up, or diagnol) for each square in the alignment matrix
  def get_traceback(self, mat):
    traceback_dict = {}
      
    # uses a double for loop to iterate through each specific location in the matrix
    for i in range(len(self.seq1)):

      #once we get to the very top positions of the matrix, the only place we can go is left
      # so we assign left to all the positions at the top of the matrix
      traceback_dict[i+1] = "left"

      for j in range(len(self.seq2)):
        #once we get to the very leftmost positions of the matrix, the only place we can go is up
        # so we assign up to all positions on the leftmost side of the matrix
        traceback_dict[int("{}0".format(j+1))] = "up"
        # gets the position of each poistion that we loop through in the matrix and stores it as an integer
        int_position = int("{}{}".format(i+1, j+1))
        # uses the equation to get the score to the left of the current matrix position
        left_check = mat[i+1][j] + self.gap_pen
        # uses the equation to get the score above the current matrix position
        up_check = mat[i][j+1] + self.gap_pen

        # uses the equation to get the score of the location diagnol to the current matrix position
        diag_check = mat[i][j] + self.blosum_mat[self.seq1[i]][self.seq2[j]]

        # takes the max value of all three of those scores we just found
        max_val = max(left_check, up_check, diag_check)

        # if the max value comes from the up position, we will store the position number and the direction it came from in a dictionary
        if max_val == up_check:
          traceback_dict[int_position] = 'up'

        # if the max value comes from the left position, we will store the position number and the direction it came from in a dictionary
        # if the up score is the same as the left score, the left will take precedence over the up
        if max_val == left_check:
          traceback_dict[int_position] = 'left'

        # if the max value comes from the diagnol position, we will store the position number and the direction it came from in a dictionary
        # if the diagnol score is the same as either the up or left score, the diagnol will take precedence over each of them
        if (max_val == diag_check):
          traceback_dict[int_position] = 'diag'

        # we then replace the current position's value in the matrix with the max value that we just found
        mat[i+1][j+1] = max_val

    # once we are done looping through and filling out the entire matrix, we then take the last value in the bottom right corner
    # and store this as a variable since this is the optimal alignment score
    opt_align_score = int(mat[len(self.seq1)][len(self.seq2)])

    # we then print out the optimal alignment score and return the traceback dictionary
    print("Optimal Alignment Score: {}".format(opt_align_score))
    return traceback_dict


  # prints out the optimal alignment between the two strings
  def get_opt_alignment(self, traceback_dict):

      # gets the length of the two sequences
      str1_len = len(self.seq1)
      str2_len = len(self.seq2)

      # creates the starting point which is the position of the last value in the matrix in the bottom right corner
      start_point = int("{}{}".format(str1_len, str2_len))
      # creates first word and second word as empty strings since we will adding to these as we go
      first_word = ''
      second_word = ''

      # uses a for loop to loop through the max amount of iterations that could happen in the worst case-scenario
      for i in range(1, (str1_len + str2_len)+1):
        # once we get to position 0,0 in the matrix which will be the same as 0, then we can break from the loop
        if start_point == 0:
          break

        # if the position that we are in has a traceback diagnolly, then we subtract one from sequence 1 and 2's length
        if traceback_dict[start_point] == 'diag':
          str1_len -= 1
          str2_len -= 1
          # we then take the first word string and add the letter in seq1 that corresponds to the index we provided
          first_word = first_word + self.seq1[str1_len]
          # we then take the second word string and add the letter in seq2 that corresponds to the index we provided
          second_word = second_word + self.seq2[str2_len]
          # we then change the start point to a new one which is the position of the matrix that we moved to diagnolly
          start_point = int("{}{}".format(str1_len, str2_len))

        # if the position that we are in has a traceback to the left, then we subtract one from sequence 2's length
        elif traceback_dict[start_point] == 'left':
          str2_len -= 1
          # we then use a dash to indicate a gap in sequence 1 since we moved to the left 
          first_word = first_word + "-"
          # we then take the second word string and add the letter in seq2 that corresponds to the index we provided
          second_word = second_word + self.seq2[str2_len]
          # we then change the start point to a new one which is the position of the matrix that we moved to, to the left
          start_point = int("{}{}".format(str1_len, str2_len))

        # if the position that we are in has a traceback upwards, then we subtract one from sequence 1's length
        elif traceback_dict[start_point] == 'up':
          str1_len -= 1
          # we then take the first word string and add the letter in seq1 that corresponds to the index we provided
          first_word = first_word + self.seq1[str1_len]
          # we then use a dash to indicate a gap in sequence 2 since we moved to the left
          second_word = second_word + "-"
          # we then change the start point to a new one which is the position of the matrix that we moved to, to the left
          start_point = int("{}{}".format(str1_len, str2_len))

      # prints the reverse of the first and second string since we were adding to the first word and second word empty strings backwards
      # so reversing them will give us the actual alignment
      print(first_word[::-1])
      print(second_word[::-1])