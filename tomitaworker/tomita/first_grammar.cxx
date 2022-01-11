#encoding "utf-8"

Person -> AnyWord<kwtype=politicians>;
Object -> AnyWord<kwtype=objects>;

Fact -> Person interp (Fact.Politician);
Fact -> Object interp (Fact.Attraction);