from rest_framework import serializers
from .models import Actor, Movie, Staff, Review

class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title',)


class StaffListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('name', 'movies',)


class ReviewSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('title',)

    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Staff
        fields = ('name', 'movies',)

class MovieSerializer(serializers.ModelSerializer):
    
    staffs = StaffSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    
    actor_pks = serializers.ListField(write_only=True)
    staff_pks = serializers.ListField(write_only=True)

    def create(self, validated_data):
        actor_pks = validated_data.pop('actor_pks')
        staff_pks = validated_data.pop('staff_pks')
        movie = Movie.objects.create(**validated_data)

        for actor_pk in actor_pks:
            movie.actors.add(actor_pk)

        for staff_pk in staff_pks:
            movie.staffs.add(staff_pk)

        return movie


    def update(self, movie, validated_data):
        actor_pks = validated_data.pop('actor_pks')
        staff_pks = validated_data.pop('staff_pks')

        for attr, value in validated_data.items():
            setattr(movie, attr, value)
            movie.save()

        movie.actors.clear()
        for actor_pk in actor_pks:
            movie.actors.add(actor_pk)

        movie.staffs.clear()
        for staff_pk in staff_pks:
            movie.staffs.add(staff_pk)

        return movie


    class Meta:
        model = Movie
        fields = '__all__'