clc;
clear;
close all;

% Simulate a clean signal (sine wave)
fs = 1000;                     % Sampling frequency
t = linspace(0, 1, fs);        % Time vector
freq = 5;                      % Frequency of sine wave
clean_signal = sin(2*pi*freq*t);

% 1. Gaussian Noise
mean_val = 0;
variance = 0.5;
gaussian_noise = mean_val + sqrt(variance) * randn(1, fs);
noisy_signal_gaussian = clean_signal + gaussian_noise;

% 2. Impulse Noise
impulse_noise = zeros(1, fs);
impulse_positions = randi([1 fs], 1, 50);
impulse_values = 5 * (2*randi([0 1], 1, 50) - 1); % Generates -5 or 5
impulse_noise(impulse_positions) = impulse_values;
noisy_signal_impulse = clean_signal + impulse_noise;

% 3. White Noise
white_noise = -1 + 2*rand(1, fs);  % Uniform distribution between -1 and 1
noisy_signal_white = clean_signal + white_noise;

% Plotting
figure;

subplot(4,1,1);
plot(t, clean_signal, 'LineWidth', 1.2);
title('Clean Signal (Sine Wave)');
xlabel('Time');
ylabel('Amplitude');
grid on;

subplot(4,1,2);
plot(t, noisy_signal_gaussian, 'LineWidth', 1.2);
title('Noisy Signal with Gaussian Noise');
xlabel('Time');
ylabel('Amplitude');
grid on;

subplot(4,1,3);
plot(t, noisy_signal_impulse, 'LineWidth', 1.2);
title('Noisy Signal with Impulse Noise');
xlabel('Time');
ylabel('Amplitude');
grid on;

subplot(4,1,4);
plot(t, noisy_signal_white, 'LineWidth', 1.2);
title('Noisy Signal with White Noise');
xlabel('Time');
ylabel('Amplitude');
grid on;

% SNR Calculation
snr_gaussian = 10 * log10(var(clean_signal) / var(gaussian_noise));
snr_impulse  = 10 * log10(var(clean_signal) / var(impulse_noise));
snr_white    = 10 * log10(var(clean_signal) / var(white_noise));

fprintf('Signal-to-Noise Ratio (SNR) with Gaussian Noise: %.2f dB\n', snr_gaussian);
fprintf('Signal-to-Noise Ratio (SNR) with Impulse Noise: %.2f dB\n', snr_impulse);
fprintf('Signal-to-Noise Ratio (SNR) with White Noise: %.2f dB\n', snr_white);