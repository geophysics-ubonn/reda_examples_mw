% Read Data
Magn = abs(Zmm);
Phas = angle(Zmm);

%Plot Data
f = figure;
set(f, 'Position', [300, 150, 1100, 500]); 

subplot(1,2,1);
semilogx(fm, Magn,'.','MarkerSize',12);
xlabel('Frequency [Hz]');
ylabel('Magnitude [Ohm]');
grid on;
xlim([min(fm) max(fm)]);

subplot(1,2,2);
semilogx(fm, -1 * Phas,'.','MarkerSize',12);
xlabel('Frequency [Hz]');
ylabel('- Phase [rad]');
grid on;
xlim([min(fm) max(fm)]);
