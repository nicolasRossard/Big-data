import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

/* Mapper counting & for each word found */
public class StubMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
	
	/* Implement the value 1 for hadoop API which allow serialization and deserialization  */
	private final static IntWritable one = new IntWritable(1);
	/* Implement  word in Text format */
	private Text word = new Text();
	
	/* We will have a tuple (word,one) */
	
	@Override
	public void map(LongWritable key, Text value, Context context)
      throws IOException, InterruptedException {
		
		//System.out.print("MAPPER");
		/* Convert the line into a String */	
		String line = value.toString();
		
		/* Break the string (so each word) into tokens */
		StringTokenizer tokenizer = new StringTokenizer(line);
		while (tokenizer.hasMoreTokens()){
			//System.out.println("----- Mapper line " +key+": " + tokenizer.toString());
			/* take the next token (¬ here it's the next word) */
			word.set(tokenizer.nextToken());
			/* Create Tuple */
			context.write(word,one);
		}
		System.out.println();
	}
	public void run (Context context) throws IOException, InterruptedException{
		/* Call at the begining of the task */
		setup(context);
		/* take back each "lines" with all informations */
		while(context.nextKeyValue()){
			map(context.getCurrentKey(),context.getCurrentValue(),context);
		}
		/* Clean the task at the end */
		cleanup(context);
	}
}
