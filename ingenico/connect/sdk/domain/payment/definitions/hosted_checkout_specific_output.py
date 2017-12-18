# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class HostedCheckoutSpecificOutput(DataObject):

    __hosted_checkout_id = None
    __variant = None

    @property
    def hosted_checkout_id(self):
        """
        | The ID of the Hosted Checkout Session in which the payment was made.
        
        Type: str
        """
        return self.__hosted_checkout_id

    @hosted_checkout_id.setter
    def hosted_checkout_id(self, value):
        self.__hosted_checkout_id = value

    @property
    def variant(self):
        """
        | The ID of the variant used to create the Hosted Checkout Session in which the payment was made.
        
        Type: str
        """
        return self.__variant

    @variant.setter
    def variant(self, value):
        self.__variant = value

    def to_dictionary(self):
        dictionary = super(HostedCheckoutSpecificOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'hostedCheckoutId', self.hosted_checkout_id)
        self._add_to_dictionary(dictionary, 'variant', self.variant)
        return dictionary

    def from_dictionary(self, dictionary):
        super(HostedCheckoutSpecificOutput, self).from_dictionary(dictionary)
        if 'hostedCheckoutId' in dictionary:
            self.hosted_checkout_id = dictionary['hostedCheckoutId']
        if 'variant' in dictionary:
            self.variant = dictionary['variant']
        return self
