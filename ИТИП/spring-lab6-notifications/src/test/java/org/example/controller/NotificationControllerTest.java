package org.example.controller;

import org.example.security.JwtService;
import org.example.service.NotificationService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@WebMvcTest(NotificationController.class)
class NotificationControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private NotificationService notificationService;

    // Мокаем зависимости безопасности
    @MockBean
    private JwtService jwtService;

    @Test
    void shouldReturnOkForGetAllNotifications() throws Exception {
        mockMvc.perform(get("/notifications/all"))
                .andExpect(status().isOk());
    }

    @Test
    void shouldReturnOkForGetNotificationById() throws Exception {
        mockMvc.perform(get("/notifications/1"))
                .andExpect(status().isOk());
    }

    @Test
    void shouldReturnOkForGetNotificationsByStatus() throws Exception {
        mockMvc.perform(get("/notifications/status/CREATED"))
                .andExpect(status().isOk());
    }

    @Test
    void shouldReturnOkForGetNotificationsByChannel() throws Exception {
        mockMvc.perform(get("/notifications/channel/EMAIL"))
                .andExpect(status().isOk());
    }

    @Test
    void shouldReturnOkForGetNotificationsByRecipient() throws Exception {
        mockMvc.perform(get("/notifications/recipient/1"))
                .andExpect(status().isOk());
    }
}
