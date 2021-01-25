import com.google.cloud.speech.v1.RecognitionAudio;
import com.google.cloud.speech.v1.RecognitionConfig;
import com.google.cloud.speech.v1.RecognitionConfig.AudioEncoding;
import com.google.cloud.speech.v1.RecognizeResponse;
import com.google.cloud.speech.v1.SpeechClient;
import com.google.cloud.speech.v1.SpeechRecognitionAlternative;
import com.google.cloud.speech.v1.SpeechRecognitionResult;
import com.google.protobuf.ByteString;

import java.io.FileWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class GoogleSpeechToText {

  /**
   * Demonstrates using the Speech API to transcribe an audio file.
   */
  public static void main(String... args) throws Exception {
    // Instantiates a client
    try (SpeechClient speechClient = SpeechClient.create()) {

      // The path to the audio file to transcribe
      String fileName = "RecordAudio.wav";
      System.out.println("Sending Data to Google Cloud Server");

      // Reads the audio file into memory
      Path path = Paths.get(fileName);
      byte[] data = Files.readAllBytes(path);
      ByteString audioBytes = ByteString.copyFrom(data);

      // Builds the sync recognize request
      RecognitionConfig config = RecognitionConfig.newBuilder()
          .setLanguageCode("en-US")
          .build();
      RecognitionAudio audio = RecognitionAudio.newBuilder()
          .setContent(audioBytes)
          .build();

      // Performs speech recognition on the audio file
      RecognizeResponse response = speechClient.recognize(config, audio);
      List<SpeechRecognitionResult> results = response.getResultsList();
      
      FileWriter file = new FileWriter("speech.txt");
      
      for (SpeechRecognitionResult result : results) {
        // There can be several alternative transcripts for a given chunk of speech. Just use the
        // first (most likely) one here.
        SpeechRecognitionAlternative alternative = result.getAlternativesList().get(0);
        String output = alternative.getTranscript();
        file.write(alternative.getTranscript().toString());
        System.out.printf("Transcription: %s%n", output);
      }
      
      file.close();
    }
    System.out.println("Done translating");
  }
}