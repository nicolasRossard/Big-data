import java.io.IOException;
import java.util.Iterator;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class StubReducer extends Reducer<Text, IntWritable, Text, DoubleWritable> {
	/* Set up the sum of each word in the file */	
	private DoubleWritable totalWordCount = new DoubleWritable();
	
	@Override
	public void reduce(final Text key, final Iterable<IntWritable> values, final Context context)
			throws IOException, InterruptedException {
		
		//System.out.println("REDUCE");
		/* Initialize sum */
		int sum =0;
		Iterator<IntWritable> iterator = values.iterator();
		
		while(iterator.hasNext()){
			//System.out.println("---- Reducer line " + key +": " +iterator);
			sum+=iterator.next().get();
		}
		totalWordCount.set(sum);
		context.write(key, totalWordCount);
  }
}
