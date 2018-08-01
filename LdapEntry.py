Entries from an LDAP user database are represented in Python as a
dictionary of key-value pairs, where each key is a case-insensitive
string object and each value is a list of bytes objects.  For example:

  ldapdict = {
      'objectclass': [b'inetOrgPerson', b'person'],
      'cn': [b'George Orwell'],
      'givenName': [b'George'],
      'sn': [b'Orwell'],
      'uidNumber': [b'1984'],
      'gidNumber': [b'1984'],
      'mail': [
      b'george.orwell@example.com',
      b'big.brother@example.com',
  ],
  }

Create an LdapEntry class with attributes for each of the keys listed
above that can be used as follows:

  e = LdapEntry(ldapdict)
  assert(e.cn == 'George Orwell')
  assert(e.uidNumber == 1984)
  assert('big.brother@example.com' in e.mail)
  assert(len(e.mail) == 2)

class LdapEntry(entry):
    """Single entry class for LDAP"""
    
    def __init__(self, entry){
        """Single entry class for LDAP
        
        Parameters:
            entry: a dict containing LDAP data, with keys:
    
        Returns:
            instance
        """
        self.objectClass = entry['objectclass']
        if not isinstance(self.objectClass, (list, tuple))
            self.objectClass = [self.objectClass]
        self.cn = entry['cn']
        self.givenName = entry['givenName']
        self.sn = entry['sn']
        self.uidNumber = entry['uidNumber']
        self.gidNumber = entry['gidNumber']
        self.mail = entry['mail']
        if not isinstance(self.mail, (list, tuple))
            self.mail = [self.mail]

    