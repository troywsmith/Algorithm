def numUniqueEmails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    uniqueEmails = []
    for email in emails:
      splitted = email.split('@')
      corrected_email = splitted[0].replace('.', '')[0:splitted[0].replace('.', '').find('+')] + '@' + splitted[1]

      if corrected_email not in uniqueEmails:
        uniqueEmails.append(corrected_email)

    return len(uniqueEmails)


print(numUniqueEmails(["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))