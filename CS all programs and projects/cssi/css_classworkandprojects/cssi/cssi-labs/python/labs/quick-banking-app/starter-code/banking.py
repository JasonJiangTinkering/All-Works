#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

class BankAccount(object):
    def __init__(self, label, balance):
        self.label = label
        self.balance = balance
        self.transactions = []

    def __str__ (self):
        return (str(self.label) + " " + str(self.balance))

    def withdraw(self, take):

        if take < self.balance and take >= 0:
            self.transactions.append(self.__str__() + " withdraw : " + str(take))
            self.balance -= take
        else:
            print('withdraw denied: not enough money')

    def deposit(self, put):
        if put >= 0:
            self.transactions.append(self.__str__() + " deposit : " + str(put))
            self.balance += put
        else: 
            print('cannot deposit negitive money')

    def rename(self, new):
        if len(new) == 0:
            
            print('new name cant be blank')

        else:
            self.transactions.append(self.__str__() + " renamed : " + new)
            self.label =  str(new)

    def transfer(self, destacc, amount):
        if amount > 0 and self.balance > amount:
            self.transactions.append(self.__str__() + " transaction of " + str(amount) + " from " + self.__str__() + " to " + destacc.__str__())
            self.withdraw(amount)
            destacc.deposit(amount)
        else: 
            print('amount cannot be negitive or exceed balance')

    def report(self):
        x = 1
        for y in self.transactions:
            
            print(x, y)
            x += 1

        return
