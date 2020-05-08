import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mrunit.mapreduce.MapDriver;
import org.apache.hadoop.mrunit.mapreduce.MapReduceDriver;
import org.apache.hadoop.mrunit.mapreduce.ReduceDriver;
import org.junit.Before;
import org.junit.Test;
import wordcount.WordCountMapper;
import wordcount.WordCountReducer;

import java.util.ArrayList;
import java.util.List;

public class TestWordCount {
    MapReduceDriver<LongWritable, Text, Text, DoubleWritable, Text, DoubleWritable> mapReduceDriver;
    MapDriver<LongWritable, Text, Text, DoubleWritable> mapDriver;
    ReduceDriver<Text, DoubleWritable, Text, DoubleWritable> reduceDriver;

    @Before
    public void setUp() {
        /*
         * Initialize mapper/reducer/mapReduce drivers
         */
        WordCountMapper mapper = new WordCountMapper();
        WordCountReducer reducer = new WordCountReducer();
        mapDriver = new MapDriver<LongWritable, Text, Text, DoubleWritable>();
        mapDriver.setMapper(mapper);
        reduceDriver = new ReduceDriver<Text, DoubleWritable, Text, DoubleWritable>();
        reduceDriver.setReducer(reducer);
        mapReduceDriver = new MapReduceDriver<LongWritable, Text, Text, DoubleWritable, Text, DoubleWritable>();
        mapReduceDriver.setMapper(mapper);
        mapReduceDriver.setReducer(reducer);
    }

    @Test
    public void testMapper() {
        Text value1 = new Text("2012-01-01\t09:00\tNew York\tMen's Clothing\t214.05\tAmex\n");
        //Text value2 = new Text("2012-01-01\t09:00\tBahamas\tMen's Clothing\t300\tAmex");

        mapDriver.withInput(new LongWritable(0),value1);
        //mapDriver.withInput(new LongWritable(1),value2);

        mapDriver.withOutput(new Text("New York"), new DoubleWritable(214.05));
        //mapDriver.withOutput(new Text("Bahamas"), new DoubleWritable(300.0));

        mapDriver.runTest();
    }

   /* @Test
    public void testMapperSeveralInputs() throws IOException {
        //Text value1 = new Text("2012-01-01\t09:00\tNew York\tMen's Clothing\t214.05\tAmex\n");
        //Text value2 = new Text("2012-01-01\t09:00\tBahamas\tMen's Clothing\t300\tAmex");
        Text val = new Text("2012-01-01\t09:00\tNew York\tToys\t25.38\tDiscover\n" +
                "2012-01-01\t09:00\tNew York\tToys\t213.88\tVisa");

        //mapDriver.withInput(new LongWritable(1),value1);
        //mapDriver.withInput(new LongWritable(2),value2);
        mapDriver.withInput(new LongWritable(0),val);
        final Pair ny =new Pair<Text,DoubleWritable>(new Text("New York"), new DoubleWritable(214.05));
        final Pair bh =new Pair<Text,DoubleWritable>(new Text("Bahamas"), new DoubleWritable(300));
        final List<Pair<Text, DoubleWritable>> result;
        result = mapDriver.run();
        assertThat(result)
                .isNotNull()
                .hasSize(2)
                .contains(ny,bh);

        mapDriver.runTest();
    }*/

    @Test
    public void testReducer() {
        List<DoubleWritable> values = new ArrayList<DoubleWritable>();
        values.add(new DoubleWritable(100.8));
        values.add(new DoubleWritable(255));
        reduceDriver.withInput(new Text("Bahamas"), values);
        reduceDriver.withOutput(new Text("Bahamas"), new DoubleWritable(355.8));
        reduceDriver.runTest();
    }

    @Test
    public void testMapReduce() {
        Text value1 = new Text("2012-01-01\t09:00\tNew York\tMen's Clothing\t214.05\tAmex\n");
        Text value2 = new Text("2012-01-01\t09:00\tBahamas\tMen's Clothing\t300\tAmex");
        Text value3 = new Text("2012-01-01\t09:00\tNew York\tMen's Clothing\t250\tAmex\n");

        mapReduceDriver.addInput(new LongWritable(0),value1);
        mapReduceDriver.addInput(new LongWritable(1),value2);
        mapReduceDriver.addInput(new LongWritable(2),value3);
        mapReduceDriver.addOutput(new Text("Bahamas"), new DoubleWritable(300));
        mapReduceDriver.addOutput(new Text("New York"), new DoubleWritable(464.05));
        mapReduceDriver.runTest();

    }

}