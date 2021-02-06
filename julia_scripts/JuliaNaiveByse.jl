using RDatasets
using Statistics
using Plots

iris = dataset("datasets", "iris")

labels = unique(iris.Species)

prior_probability(label) = sum(iris.Species.==label)/length(iris.Species)
p_y = [
    prior_probability(labels[1]) # "setosa"
    prior_probability(labels[2]) # "versicolor"
    prior_probability(labels[3]) # "virginica"
]

function average_label(label)
    mean_label = [
        mean(iris[iris.Species.==label, :SepalLength])
        mean(iris[iris.Species.==label, :SepalWidth])
        mean(iris[iris.Species.==label, :PetalLength])
        mean(iris[iris.Species.==label, :PetalWidth])
        ]
    return mean_label
end

function variance_label(label)
    var_label = [
        var(iris[iris.Species.==label, :SepalLength])
        var(iris[iris.Species.==label, :SepalWidth])
        var(iris[iris.Species.==label, :PetalLength])
        var(iris[iris.Species.==label, :PetalWidth])
        ]
    return var_label
end

means = [average_label(labels[1]), average_label(labels[2]), average_label(labels[3])]
variance = [variance_label(labels[1]), variance_label(labels[2]), variance_label(labels[3])]

gaussian(x, μ, σ²) = exp.((x - μ).^2 ./ 2σ²) ./ sqrt.(2*π*σ²)
label_probability = zeros(length(labels))

true_label = zeros(Int64, size(iris)[1])

for i in 1:size(iris)[1]
    for j in [1,2,3]
        x = [iris[i, :SepalLength], iris[i, :SepalWidth], iris[i, :PetalLength], iris[i, :PetalWidth]]
        label_probability[j] = p_y[j] * prod(gaussian(x, means[j], variance[j]))
    true_label[i] = findall(label_probability .== minimum(label_probability))[1]
    end
end

count_true = 0
for i in 1:1:size(iris)[1]
    global count_true
    if labels[true_label[i]] == iris.Species[i]
        count_true += 1
    end
end

println(count_true/length(iris.Species))
