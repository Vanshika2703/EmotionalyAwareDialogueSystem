import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Collection;
import java.util.List;
import java.util.Properties;
import java.util.Scanner;
import edu.stanford.nlp.ie.util.RelationTriple;
import edu.stanford.nlp.ling.CoreAnnotations.*;
import edu.stanford.nlp.naturalli.NaturalLogicAnnotations;
import edu.stanford.nlp.pipeline.*;
import edu.stanford.nlp.util.CoreMap;

public class NLPPosted {

	public static void main(String[] args) throws IOException {

		Properties props = new Properties();
		props.put("annotators", "tokenize, ssplit, pos, lemma, depparse, natlog, openie");

		StanfordCoreNLP pipeline = new StanfordCoreNLP(props);
		// read some text in the text variable
		// String text = "Fred and David Bark are with me.";
//        String text = "Pick up the blue block.";
//        String text = "In 1921, Einstein received the Nobel Prize for his original work on the photoelectric effect."; 
//        String text = "Did Einstein receive the Nobel Prize?"; 
		// String text = "Mary saw a ring through the window and asked John for it.";
		// create an empty Annotation just with the given text
		File inputFile = new File("lincoln.txt");
		Scanner scanner = new Scanner(inputFile);
		BufferedWriter writer = new BufferedWriter(new FileWriter("lincolnOUT.txt"));
		int current = 1;

		writer.write("Sentence: 0" + "\t" + "[subject, predicate, object, confidence level] \n");
		writer.write(" ");
		writer.newLine();
		writer.write(" ");
		writer.newLine();
		
		while (scanner.hasNext()) {
			Annotation document = new Annotation(scanner.nextLine());

			// run all Annotators on this text
			pipeline.annotate(document);

			// these are all the sentences in this document
			// a CoreMap is essentially a Map that uses class objects as keys and has values
			// with custom types
			List<CoreMap> sentences = document.get(SentencesAnnotation.class);
			
			for (CoreMap sentence : sentences) {
				// traversing the words in the current sentence
				// a CoreLabel is a CoreMap with additional token-specific methods

				Collection<RelationTriple> triples = sentence
						.get(NaturalLogicAnnotations.RelationTriplesAnnotation.class);

				for (RelationTriple triple : triples) {
					writer.write("Sentence: " + current + "\t" + "[" + triple.subjectGloss() + ","
							+ triple.relationGloss() + "," + triple.objectGloss() + "," + triple.confidence + "]  \n");
					writer.newLine();
				}
				writer.write(" ");
				writer.newLine();

				current++;

			}
		}

		writer.close();
		scanner.close();

	}

}