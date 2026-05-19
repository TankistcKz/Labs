package org.example.mapper;

import org.example.model.dto.UserDto;
import org.example.model.entity.User;
import org.springframework.stereotype.Component;

@Component
public class UserMapper {

    public UserDto toDto(User user) {
        return UserDto.builder()
                .name(user.getName())
                .email(user.getEmail())
                .phone(user.getPhone())
                .deviceToken(user.getDeviceToken())
                .telegramChatId(user.getTelegramChatId())
                .createdAt(user.getCreatedAt())
                .build();
    }

    public User toEntity(UserDto userDto) {
        User user = new User();
        user.setName(userDto.getName());
        user.setEmail(userDto.getEmail());
        user.setPhone(userDto.getPhone());
        user.setDeviceToken(userDto.getDeviceToken());
        user.setTelegramChatId(userDto.getTelegramChatId());
        user.setCreatedAt(userDto.getCreatedAt());
        return user;
    }
}
