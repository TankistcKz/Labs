package org.example.service;

import java.util.List;
import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;

@Service
public class NotificationManager {
//     private final MessageService messageService;
// 
// 	@Autowired
// 	public NotificationManager(@Qualifier("CustomEmail") MessageService messageService) {
//         this.messageService = messageService;
//     }
// 
//     public void notify(String message, String recipient) {
//         messageService.sendMessage(message, recipient);
//     }


    private final List<MessageService> messageServices;

    @Autowired
    public NotificationManager(List<MessageService> messageServices) {
        this.messageServices = messageServices;
    }

    public void notify(String message, String recipient) {
        messageServices.forEach(service -> service.sendMessage(message, recipient));
    }
}
