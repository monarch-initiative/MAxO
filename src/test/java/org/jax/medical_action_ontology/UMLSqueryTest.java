package org.jax.medical_action_ontology;

import org.junit.BeforeClass;
import org.junit.Test;
import uts.rest.api.util.RestTicketClient;
import org.junit.Assert.*;

import static org.junit.Assert.*;

public class UMLSqueryTest {

    @BeforeClass
    public static void setup() {

        String API_KEY = "2fefdd14-3870-4009-b1c2-59c9e1b7e4fd";
        RestTicketClient ticketClient = new RestTicketClient(API_KEY);
        String ticket = ticketClient.getTgt();
        String version = "2017AB";
    }

    @Test
    public void querySeizure() throws Exception {

        String query_term = "seizure";
        int result_size = UMLSquery.query(query_term).size();
        assertEquals(2, result_size);

    }
    @Test
    public void queryBlind() throws Exception {

        String query_term = "blind";
        int result_size = UMLSquery.query(query_term).size();
        assertEquals(5, result_size);

    }
    @Test
    public void queryHearing() throws Exception {

        String query_term = "hearing loss";
        int result_size = UMLSquery.query(query_term).size();
        assertEquals(5, result_size);

    }
    @Test
    public void queryUV() throws Exception {

        String query_term = "UV";
        int result_size = UMLSquery.query(query_term).size();
        assertEquals(3, result_size);

    }
    @Test
    public void queryXedeg() throws Exception {

        String query_term = "xedeg";
        int result_size = UMLSquery.query(query_term).size();
        assertEquals(0, result_size);

    }


}