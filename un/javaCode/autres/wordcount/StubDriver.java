import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;
//import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;

public class StubDriver extends Configured implements Tool{
	public int run(String[] args) throws Exception {

    /*
     * Validate that two arguments were passed from the command line.
     */
    if (args.length != 2) {
      System.out.printf("Usage: StubDriver <input dir> <output dir>\n");
      System.exit(-1);
    }
    
    /*
     * Instantiate a Job object for your job's configuration. 
     * Specify an easily-decipherable name for the job.
     * This job name will appear in reports and logs.
     *
     */
    Job job = Job.getInstance(getConf(), "Stub Driver");
    
     /*
     * Specify the jar file that contains your driver, mapper, and reducer.
     * Hadoop will transfer this jar file to nodes in your cluster running 
     * mapper and reducer tasks.
     */
    job.setJarByClass(StubDriver.class);
    job.setMapperClass(StubMapper.class);
    job.setReducerClass(StubReducer.class);
   
   /* 
    * Define tuple's types in output 
    */
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    
    /* 
     * Path of files input and output 
     */
    Path inputFilePath =new Path(args[0]);
    Path outputFilePath = new Path(args[1]);
    
    /*
     * Recursive on
     */ 
    FileInputFormat.setInputDirRecursive(job, true);
    
    FileInputFormat.addInputPath(job, inputFilePath);
    FileOutputFormat.setOutputPath(job, outputFilePath);
    FileSystem fs = FileSystem.newInstance(getConf());
    
    /* 
    * Delete outputFilePath if it already exists
    */  
    if(fs.exists(outputFilePath)){
    	fs.delete(outputFilePath,true);
    }
    
    
    /*
     * Start the MapReduce job and wait for it to finish.
     * If it finishes successfully, return 0. If not, return 1.
     */
    return job.waitForCompletion(true) ? 0: 1;
  }
  
  public static void main(String[] args) throws Exception {
	  StubDriver stubDriver = new StubDriver();
	  int res = ToolRunner.run( stubDriver,  args);
	  System.exit(res);
  }
}

