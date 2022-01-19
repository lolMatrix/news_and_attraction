#encoding "utf-8"

Person -> Word<kwtype=politicians>;
Object -> Word<kwtype=objects>;

Fact -> Person interp (Fact.Politician::not_norm);
Fact -> Object interp (Fact.Attraction::not_norm);