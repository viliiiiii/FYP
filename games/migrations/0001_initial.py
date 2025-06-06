# Generated by Django 5.0.4 on 2025-04-26 17:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchPoll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.IntegerField(unique=True)),
                ('home_team', models.CharField(max_length=100)),
                ('away_team', models.CharField(max_length=100)),
                ('home_team_crest', models.URLField(blank=True, max_length=500, null=True)),
                ('away_team_crest', models.URLField(blank=True, max_length=500, null=True)),
                ('match_date', models.DateTimeField()),
                ('is_closed', models.BooleanField(default=False)),
                ('correct_outcome', models.CharField(blank=True, choices=[('HOME', 'Home Win'), ('DRAW', 'Draw'), ('AWAY', 'Away Win')], max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['match_date'],
            },
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_a', models.CharField(max_length=255)),
                ('option_b', models.CharField(max_length=255)),
                ('option_c', models.CharField(max_length=255)),
                ('option_d', models.CharField(max_length=255)),
                ('correct_answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='medium', max_length=10)),
                ('category', models.CharField(choices=[('history', 'Liga History'), ('players', 'Players'), ('teams', 'Teams'), ('stats', 'Statistics'), ('current', 'Current Season')], default='current', max_length=20)),
                ('explanation', models.TextField(blank=True, null=True)),
                ('points', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='QuizAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(choices=[('regular', 'Regular'), ('hard', 'Hard')], default='regular', max_length=10)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('score', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('time_taken', models.DurationField(blank=True, null=True)),
                ('accuracy', models.FloatField(default=0)),
                ('avg_response_time', models.DurationField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_attempts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-start_time'],
            },
        ),
        migrations.CreateModel(
            name='QuestionResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_answer', models.CharField(blank=True, max_length=1, null=True)),
                ('is_correct', models.BooleanField(default=False)),
                ('response_time', models.DurationField(blank=True, null=True)),
                ('quiz_attempt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.quizattempt')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.quizquestion')),
            ],
            options={
                'unique_together': {('quiz_attempt', 'question')},
            },
        ),
        migrations.AddField(
            model_name='quizattempt',
            name='questions',
            field=models.ManyToManyField(through='games.QuestionResponse', to='games.quizquestion'),
        ),
        migrations.CreateModel(
            name='PollVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction', models.CharField(choices=[('HOME', 'Home Win'), ('DRAW', 'Draw'), ('AWAY', 'Away Win')], max_length=10)),
                ('is_correct', models.BooleanField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='games.matchpoll')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('poll', 'user')},
            },
        ),
        migrations.CreateModel(
            name='QuizScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(choices=[('regular', 'Regular'), ('hard', 'Hard')], max_length=10)),
                ('score', models.FloatField()),
                ('date_achieved', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_scores', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-score'],
                'unique_together': {('user', 'mode')},
            },
        ),
    ]
