
package org.jax.medical_action_ontology;
import uts.rest.api.util.RestTicketClient;
import uts.rest.api.classes.*;

import java.io.*;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.util.*;

import com.jayway.jsonpath.Configuration;
import com.jayway.jsonpath.JsonPath;
import com.jayway.restassured.RestAssured;
import com.jayway.restassured.response.Response;
import com.jayway.jsonpath.spi.mapper.JacksonMappingProvider;

import static com.jayway.restassured.RestAssured.given;


public class UMLSquery implements Runnable {

	static String API_KEY = "2fefdd14-3870-4009-b1c2-59c9e1b7e4fd";
	static RestTicketClient ticketClient = new RestTicketClient(API_KEY);
	static String ticket = ticketClient.getTgt();
	static String version = "2017AB";
	static String outdir = "main/resources/Ontology_Terms/Multithreading_test/";
	private Path file;

	public UMLSquery(Path file) {
		this.file = file;
	}

	public static ArrayList<SearchResult> query(String term) {

		int pageNumber = 0;
		SearchResult[] results;
		ArrayList<SearchResult> all = new ArrayList<SearchResult>();

		do {
			pageNumber++;
			System.out.printf("Fetching result for page $d: \n", pageNumber);
			RestAssured.baseURI = "https://uts-ws.nlm.nih.gov";
			Response response = given()
					.request().with()
						.param("ticket", ticketClient.getST(ticket))
						.param("string", term)
						.param("pageNumber", pageNumber)
						.param("searchType", "exact")
						.param("returnIdType", "sourceUi")
					.expect()
						.statusCode(200)
					.when().get("rest/search/" + version);

			String output = response.getBody().asString();

			Configuration config = Configuration.builder().mappingProvider(new JacksonMappingProvider()).build();
			results = JsonPath.using(config).parse(output).read("$.result.results",SearchResult[].class);

			for (SearchResult result : results) {

				if (!result.getUi().equals("NONE")) {
					all.add(result);
				}
			}

		} while(!results[0].getUi().equals("NONE"));

		return  all;

	}

	public static String sourceOnco(ArrayList<SearchResult> results) {
		StringJoiner sourceOncos = new StringJoiner("\t");
		for (SearchResult result : results) {
			List<String> ouput_str = Arrays.asList(result.getUi(), result.getName(), result.getRootSource());
			sourceOncos.add(String.join("//", ouput_str));
		}
		return sourceOncos.toString();
	}

	public void run() {

		Path outfile = Paths.get(outdir + this.file.getFileName());
		try (BufferedReader reader = Files.newBufferedReader(this.file);
			 BufferedWriter writer = Files.newBufferedWriter(outfile)) {
			String line = null;
			while ((line = reader.readLine()) != null && line.length() != 0) {
				String[] elems = line.split("\t");
				String umls_query_result = sourceOnco(query(elems[0]));
				writer.write(elems[0] + "\t" + umls_query_result + "\n");
			}
		} catch (IOException e) {
			System.out.println("File not exist");
		}

	}

	

}
