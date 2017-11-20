package org.jax.medical_action_ontology;
import com.jayway.restassured.RestAssured;
import com.jayway.restassured.response.Response;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import static com.jayway.restassured.RestAssured.given;


public class BioPortalquery {

    private static final String api_key = "7a8590b9-b311-48a8-8122-f913830c7599";
    static String outdir_path = "src/main/resources/Ontology_Terms/Most_Frequent_Sens_and_BioPortalxref/";

    public BioPortalquery() {
        Path outdir = Paths.get(outdir_path);
        try {
            Files.createFile(outdir);
        } catch (FileAlreadyExistsException e) {
            System.out.println("File already exist! \n Continue...");
        } catch (IOException e) {
            System.out.println("Incorrect file path!");
        }
    }

    public static void query(String term) {

        int pageNumber = 2;
        System.out.printf("Fetching result for page %d: \n", pageNumber);
        RestAssured.baseURI = "http://data.bioontology.org";
        Response response = given()
                .request().with()
                    .param("apikey", api_key)
                    .param("include", "prefLabel")
                    //.param("with_exact_match", true)
                    .param("pageNumber", pageNumber)
                    .param("pagesize", 50)
                    //.param("include_views", true) //unsure what it does
                    .param("include_views", false)
                    .param("display_context", false)
                    .param("display_links", false)
                .expect()
                    .statusCode(200)
                .get("search?q=" + term);

        String output = response.getBody().asString();

        System.out.println(output);

    }

    public static void main(String[] args) {
        query("alcohol");
    }

}
