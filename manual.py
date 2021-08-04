def syntax(specify):
  phrase = "The proper syntax of this command is as follows: "
  note = "\n\n_As with all man commands (excluding 'custom'), you can use \"\" to insert an indefinite amount of words as a phrase._"
  if specify=='announce':
    return ("The proper syntax of this command is as follows: '>announce [title] [description] [Optional: URL]'\n\n\nPlease use double quotes when specifying all fields.\n\nNote: There is currently limited functionality for the the amount of fields. Please wait for a later update.\nAt the moment, the embed color can't be changed and is set to blue. To input multiple URLs, simply enter a space between each one.\n\nEmbed Specification has been removed, please use custom instead if that part is required." + note)
  elif specify=='caesar':
    return "The proper syntax of this command is as follows: '>caesar [phrase/word] [shift]'\n\nWith 'shift' indicating the amount of times the cipher will move forward in the alphabet. Note: this command currently has no support for backward shifts" + note
  elif specify=='spam':
    return phrase + "'>spam [phrase/word] [amount] [interval]'\n\nWith 'amount' indicating the amount of times the word is repeated, and with 'interval' indicating the amount of time between each repeat.\nInterval is represented in seconds where '1' would be 1 second and '0.5' would be half a second." + note
  else:
    return "There is no 'man' page for that command."