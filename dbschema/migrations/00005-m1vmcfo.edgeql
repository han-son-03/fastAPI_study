CREATE MIGRATION m1vmcfojstn5tbxkpxrcoe5a4nrpb465m4u33gzxswsxgb2t5qfihq
    ONTO m1radfpuucibl4i4h75y3dliykmvfqc2mawa2hdgiyrdxgd3dvtndq
{
  ALTER TYPE default::Meeting {
      CREATE PROPERTY end_date: cal::local_date;
      CREATE REQUIRED PROPERTY location: std::str {
          SET default := '';
      };
      CREATE PROPERTY start_date: cal::local_date;
      CREATE REQUIRED PROPERTY title: std::str {
          SET default := '';
      };
  };
};
