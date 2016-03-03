import java.io.File;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.PrintWriter;
import java.io.IOException;

public class Extract{
	public static void main(String[] args)throws IOException{
		String inputfile = "source.txt";
		FileReader fr = null;
	    BufferedReader br = null;
	    File file = new File("extract.txt");
	    FileWriter fw = new FileWriter(file);
	    BufferedWriter bw = new BufferedWriter(fw);
	    PrintWriter pw = new PrintWriter(bw);
	    int count=1;
	    try {
	        fr = new FileReader(inputfile);
	        br = new BufferedReader(fr);

	        String line;
	        while ((line = br.readLine()) != null) {
	        	if(line.indexOf("@")==-1 && (line = br.readLine()) != null){
	        		pw.print("[" + count + "]");
	        		while(line.indexOf("件のリツイート")==-1 && line != null){
	        			pw.println(line);
	        			line = br.readLine();
	        		}
	        		pw.println("");
	        		count++;
	        	}
	            System.out.println(line);
	        }
	    } catch (FileNotFoundException e) {
	        e.printStackTrace();
	    } catch (IOException e) {
	        e.printStackTrace();
	    } finally {
	        try {
	            br.close();
	            fr.close();
	            bw.close();
	            fw.close();
	        } catch (IOException e) {
	            e.printStackTrace();
	        }
	    }
	}
}
