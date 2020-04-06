import unittest
import uuid
from gset import GSet
from twoPSet import TwoPSet

class NodeOperations:

    def setUp(self,gset,n):
        id1=uuid.uuid4()
        gset[n] = GSet(id1)
        id2=uuid.uuid4()
        twoPSet[n] = TwoPSet(id2)

    def test_querying_gset_with_merging(self,n1,n2):
        self.gset[n2].merge(self.gset[n1])
        for i in self.gset[n1].payload:
            self.assertTrue(self.gset[n2].query(i), msg="Values not copied completely")
        self.gset[n1].merge(self.gset[n2])
        for i in self.gset[n2].payload:
            self.assertTrue(self.gset[n1].query(i), msg="Values not copied completely")

    def test_merging_twopset_with_removal(self,n1,n2):
        self.twoPSet[n2].merge(self.twoPSet[n1])
        for i in self.twoPSet[n1].A.payload:
            self.assertTrue(self.gset[n2].A.query(i), msg="Values not copied completely")
        for i in self.twoPSet[n1].B.payload:
            self.assertTrue(self.gset[n2].A.query(i), msg="Values not copied completely")
        self.twoPSet[n1].merge(self.twoPSet[n2])
        for i in self.twoPSet[n2].A.payload:
            self.assertTrue(self.gset[n1].A.query(i), msg="Values not copied completely")
        for i in self.twoPSet[n2].B.payload:
            self.assertTrue(self.gset[n1].B.query(i), msg="Values not copied completely")